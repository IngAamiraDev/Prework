import os
import json
import shutil
import uuid
from datetime import datetime
from decimal import Decimal
from concurrent.futures import ThreadPoolExecutor

class SplitS3:
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
        channel_index = 0
        while True:
            s3_path = f"{self.path_data}/s3/{self.channel_name}-{channel_index}"
            if not os.path.exists(s3_path):
                break

            dynamodb_path = self._create_directory(f"{self.path_data}/dynamodb/{self.channel_name}-{channel_index}")
            data_by_date, keys_to_delete, processed_files, events_num = {}, [], [], 0

            print(f"Processing files for {s3_path}")
            for filename in filter(lambda f: f.endswith(".json"), os.listdir(s3_path)):
                if events_num >= self.max_events_num:
                    break
                full_name = os.path.join(s3_path, filename)
                with open(full_name, "r", encoding="utf-8") as file:
                    for event in json.load(file):
                        event_date = self._get_date(event)
                        data_by_date.setdefault(event_date, []).append(json.dumps(event, cls=JSONEncoder))
                        keys_to_delete.append({
                            "user_id": event["user_id"],
                            "event_id": event["event_id"]
                        })
                        events_num += 1
                    processed_files.append(full_name)

            self._save_data_by_date(data_by_date, channel_index)
            self._save_keys_to_delete(keys_to_delete, dynamodb_path, processed_files)
            self._clean_processed_files(s3_path)
            channel_index += 1

    def _save_data_by_date(self, data_by_date, channel_index):
        """Save data split by date using threads"""
        print("Saving data split by date...")
        with ThreadPoolExecutor(max_workers=self.threads_num) as executor:
            for result in executor.map(
                    lambda item: self._save_file_to_disk(item, channel_index),
                    data_by_date.items()
            ):
                self.total_size += result

    def _save_file_to_disk(self, item, channel_index):
        """Save data split by date and return file size"""
        date, events = item
        path = self._create_directory(f"{self.path_data}/s3/upload/{self.channel_name}-{channel_index}/unprocessed/{date}")
        file_path = f"{path}/{uuid.uuid4()}"
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(events, file)
        return os.path.getsize(file_path)

    def _save_keys_to_delete(self, keys, dynamodb_path, processed_files):
        """Save keys to delete"""
        print("Saving keys to delete...")
        self._write_json_file(f"{dynamodb_path}/{uuid.uuid4()}.json", keys)
        self._write_json_file(f"{dynamodb_path}/names_processed.delete",
                              [os.path.normpath(path).replace("\\", "/") for path in processed_files])

    def _clean_processed_files(self, s3_path):
        """Remove processed directory"""
        print(f"Deleting files in {s3_path}...")
        shutil.rmtree(s3_path, ignore_errors=True)

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
    """Clase para serializar objetos de tipo Decimal."""
    def default(self, o):
        """Serializa objetos de tipo Decimal."""
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)