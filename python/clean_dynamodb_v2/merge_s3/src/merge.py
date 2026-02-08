import os
import shutil
import zipfile
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

class MergeSubdir:
    """Class to merge subdirectories, extract zip files, and upload to S3"""

    def __init__(self, channel_name, path_data):
        self.channel_name = channel_name
        self.path_data = path_data

    def merge_s3_zip(self):
        """Extract all zip files in the upload directory"""
        upload_path = os.path.join(self.path_data, "upload")
        zip_files = [f for f in os.listdir(upload_path) if f.endswith(".zip")]

        for zip_file in zip_files:
            zip_path = os.path.join(upload_path, zip_file)
            target_path = os.path.join(upload_path, zip_file.replace(".zip", ""))
            os.makedirs(target_path, exist_ok=True)

            logging.info(f"Extracting {zip_path} into {target_path}...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(target_path)

            logging.info(f"Deleting zip file: {zip_path}...")
            os.remove(zip_path)

    def merge_s3(self):
        """Merge subdirectories into a single directory"""
        logging.info(f"Merging directories for channel: {self.channel_name}")
        base_consolidated_path = os.path.join(self.path_data, "upload", self.channel_name, "unprocessed")
        subdirectories = [d for d in os.listdir(os.path.join(self.path_data, "upload")) if d.startswith(f"{self.channel_name}-")]
        for subdir in subdirectories:
            source_base_path = os.path.join(self.path_data, "upload", subdir, "unprocessed")
            if not os.path.exists(source_base_path):
                continue

            for date_folder in os.listdir(source_base_path):
                source_path = os.path.join(source_base_path, date_folder)
                consolidated_path = os.path.join(base_consolidated_path, date_folder)
                os.makedirs(consolidated_path, exist_ok=True)

                for filename in os.listdir(source_path):
                    source_file = os.path.join(source_path, filename)
                    destination_file = os.path.join(consolidated_path, filename)
                    shutil.move(source_file, destination_file)

            source_base_path = os.path.join(self.path_data, "upload", subdir)
            logging.info(f"Deleting directory: {source_base_path}...")
            shutil.rmtree(source_base_path)

    def process(self):
        """Execute the extraction, merge, and upload process"""
        self.merge_s3_zip()
        self.merge_s3()