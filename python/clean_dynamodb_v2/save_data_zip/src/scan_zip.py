import os
import zipfile
import logging
import re

MAX_ZIP_SIZE = 5 * 1024 * 1024 * 1024  # 5GB

class ScanS3Zip:
    """Class to handle S3 zip file operations."""

    def __init__(self, source_dir, zip_prefix):
        self.source_dir = source_dir
        self.zip_prefix = zip_prefix

    def split_and_zip(self):
        # Buscar los zips existentes y el último índice
        zip_dir = os.path.dirname(self.zip_prefix)
        zip_base = os.path.basename(self.zip_prefix)
        existing_zips = [
            f for f in os.listdir(zip_dir)
            if re.match(rf"{re.escape(zip_base)}-(\d+)\.zip$", f)
        ]
        if existing_zips:
            last_index = max(
                int(re.search(r"-(\d+)\.zip$", f).group(1))
                for f in existing_zips
            )
            last_zip_path = os.path.join(zip_dir, f"{zip_base}-{last_index}.zip")
            current_zip_size = os.path.getsize(last_zip_path)
            # Si el último zip ya está lleno, empieza uno nuevo
            if current_zip_size >= MAX_ZIP_SIZE:
                zip_index = last_index + 1
                current_zip_size = 0
                current_zip_path = os.path.join(zip_dir, f"{zip_base}-{zip_index}.zip")
                zip_file = zipfile.ZipFile(current_zip_path, "w", zipfile.ZIP_DEFLATED)
                logging.info(f"Creando zip: {current_zip_path}")
            else:
                zip_index = last_index
                current_zip_path = last_zip_path
                zip_file = zipfile.ZipFile(current_zip_path, "a", zipfile.ZIP_DEFLATED)
                logging.info(f"Abriendo zip existente: {current_zip_path} (tamaño: {current_zip_size} bytes)")
        else:
            zip_index = 0
            current_zip_size = 0
            current_zip_path = f"{self.zip_prefix}-{zip_index}.zip"
            zip_file = zipfile.ZipFile(current_zip_path, "w", zipfile.ZIP_DEFLATED)
            logging.info(f"Creando zip: {current_zip_path}")

        json_files = [
            os.path.join(self.source_dir, f)
            for f in os.listdir(self.source_dir)
            if f.endswith(".json") and os.path.isfile(os.path.join(self.source_dir, f))
        ]
        json_files.sort()

        for json_file in json_files:
            file_size = os.path.getsize(json_file)
            if current_zip_size + file_size > MAX_ZIP_SIZE:
                zip_file.close()
                logging.info(f"Zip finalizado: {current_zip_path} (tamaño: {current_zip_size} bytes)")
                zip_index += 1
                current_zip_path = f"{self.zip_prefix}-{zip_index}.zip"
                zip_file = zipfile.ZipFile(current_zip_path, "w", zipfile.ZIP_DEFLATED)
                logging.info(f"Creando zip: {current_zip_path}")
                current_zip_size = 0
            zip_file.write(json_file, arcname=os.path.basename(json_file))
            current_zip_size += file_size
            logging.info(f"Añadido {json_file} ({file_size} bytes) a {current_zip_path}")
            os.remove(json_file)
            logging.info(f"Eliminado {json_file} del directorio original")

        zip_file.close()
        logging.info(f"Zip finalizado: {current_zip_path} (tamaño: {current_zip_size} bytes)")

    def process(self):
        """Execute the extraction zip process"""
        self.split_and_zip()