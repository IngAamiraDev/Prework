import os
import json
import re
import shutil
import uuid
import zipfile
import logging
from datetime import datetime
from decimal import Decimal
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

class SplitS3Zip:
    """Separate files by date"""

    def __init__(self, path_data, channel_name, max_date, threads_num, max_events_num):
        self.path_data = path_data
        self.channel_name = channel_name
        self.max_timestamp = datetime.strptime(max_date, "%Y-%m-%d").timestamp()
        self.max_events_num = max_events_num
        self.total_size = 0
        self.threads_num = threads_num

    def process(self):
        """Process files and split by date"""
        upload_path = os.path.join(self.path_data, "s3")
        zip_files = [
            f for f in os.listdir(upload_path)
            if f.endswith(".zip") and re.match(rf"{self.channel_name}-\d+\.zip", f)
        ]

        for zip_file in zip_files:
            channel_index = zip_file.split('-')[-1].split('.')[0]
            zip_path = os.path.join(upload_path, zip_file)
            s3_path = os.path.join(self.path_data, "s3", f"{self.channel_name}-{channel_index}")
            dynamodb_path = self._create_directory(os.path.join(self.path_data, "dynamodb", f"{self.channel_name}-{channel_index}"))
            data_by_date, keys_to_delete, processed_files, events_num = {}, [], [], 0
            self._unzip_file(zip_path, s3_path)
            self._process_json_files(s3_path, data_by_date, keys_to_delete, processed_files, events_num) #TODO: Optimize this method to handle large files more efficiently
            self._save_data_by_date(data_by_date, channel_index)
            self._save_keys_to_delete(keys_to_delete, dynamodb_path, processed_files) #TODO: Optimize this method to handle large files more efficiently
            self._clean_processed_files(s3_path) #TODO: Fix this method to handle large files more efficiently
            self._ziper_processed_files(self.path_data)

    def _unzip_file(self, zip_path, s3_path):
        """Unzip a file into the specified directory."""
        self._create_directory(s3_path)
        logging.info(f"Unzipping {zip_path} into {s3_path}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for file in zip_ref.namelist():
                file_name = os.path.basename(file)
                target_path = os.path.join(s3_path, file_name)
                zip_ref.extract(file, s3_path)
                extracted_file_path = os.path.join(s3_path, file)

                if not os.path.exists(target_path):
                    os.rename(extracted_file_path, target_path)

    def _process_json_files(self, s3_path, data_by_date, keys_to_delete, processed_files, events_num):
        """Process JSON files in the specified directory."""
        logging.info(f"Processing files for {s3_path}")
        json_files = [os.path.join(s3_path, f) for f in os.listdir(s3_path) if f.endswith(".json")]
        for full_name in json_files:
            if events_num >= self.max_events_num:
                break
            try:
                with open(full_name, "r", encoding="utf-8") as file:
                    events = json.load(file)
                    for event in events:
                        event_date = self._get_date(event)
                        event_json = json.dumps(event, cls=JSONEncoder)
                        data_by_date.setdefault(event_date, []).append(event_json)
                        keys_to_delete.append({
                            "user_id": event["user_id"],
                            "event_id": event["event_id"]
                        })
                        events_num += 1
                        if events_num >= self.max_events_num:
                            break
                processed_files.append(full_name)
            except (json.JSONDecodeError, KeyError) as e:
                logging.error(f"Error processing file {full_name}: {e}")
                continue

        return events_num

    def _save_data_by_date(self, data_by_date, channel_index):
        """Save data split by date using threads"""
        logging.info("Saving data split by date...")
        with ThreadPoolExecutor(max_workers=self.threads_num) as executor:
            for result in executor.map(
                    lambda item: self._save_file_to_disk(item, channel_index),
                    data_by_date.items()
            ):
                self.total_size += result

    def _save_file_to_disk(self, item, channel_index):
        """Save data split by date and return file size"""
        date, events = item
        path = self._create_directory(os.path.join(self.path_data, "s3", "upload", f"{self.channel_name}-{channel_index}", "unprocessed", date))
        file_path = os.path.join(path, f"{uuid.uuid4()}.json")
        logging.debug(f"Saving file to: {file_path}")
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(events, file)
        return os.path.getsize(file_path)

    def _ziper_processed_files(self, base_path):
        """Zip processed files"""
        upload_path = os.path.join(base_path, "s3", "upload")
        logging.info(f"Processing files for {upload_path}")

        for folder in os.listdir(upload_path):
            folder_path = os.path.join(upload_path, folder)
            if folder_path.endswith(".zip"):
                logging.warning(f"Skipping already zipped folder: {folder_path}")
                continue

            zip_path = f"{folder_path}.zip"
            logging.info(f"Creating zip for: {folder_path}")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        json_path = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, json_path)
            logging.info(f"Zip created: {zip_path}")
            logging.info(f"Deleting files in {folder_path}...")
            shutil.rmtree(folder_path, ignore_errors=True)

    def _save_keys_to_delete(self, keys, dynamodb_path, processed_files):
        """Save keys to delete"""
        logging.info("Saving keys to delete...")
        self._write_json_file(os.path.join(dynamodb_path, f"{uuid.uuid4()}.json"), keys)

    def _clean_processed_files(self, s3_path):
        """Remove processed directory and zip file."""
        logging.info(f"Deleting directory and zip file in {s3_path}...")
        if os.path.exists(s3_path):
            shutil.rmtree(s3_path, ignore_errors=True)
        else:
            logging.warning(f"Directory not found: {s3_path}")

        zip_file = f"{s3_path}.zip"
        if os.path.exists(zip_file):
            logging.info(f"Deleted zip file: {zip_file}")
            os.remove(zip_file)
        else:
            logging.warning(f"Zip file not found: {zip_file}")

    def _get_date(self, event):
        """Extract event date"""
        return datetime.fromtimestamp(float(event["timestamp"])).strftime("%Y-%m-%d")

    def _create_directory(self, path):
        """Create directory if it doesn't exist"""
        os.makedirs(path, exist_ok=True)
        return path

    def _write_json_file(self, path, data):
        """Write JSON data to file"""
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file)

class JSONEncoder(json.JSONEncoder):
    """Class to serialize Decimal objects."""
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)