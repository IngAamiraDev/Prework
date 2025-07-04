import os
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

class CleanFile:
    def __init__(self, file_delete, upload_file, cleaned_file_path):
        self.file_name = file_delete
        self.upload_file = upload_file
        self.cleaned_file_path = cleaned_file_path

    def create_data(self):
        """Create a cleaned file with full paths from the upload file"""
        try:
            with open(self.upload_file, "r") as file, open(self.cleaned_file_path, "w") as output_file:
                for line in file:
                    if "upload: " in line:
                        start_index = line.find("upload: ") + len("upload: ")
                        end_index = line.find(" to ")
                        relative_path = line[start_index:end_index].strip()
                        full_path = os.path.join(self.file_name, relative_path)
                        output_file.write(f"{full_path}\n")
        except Exception as e:
            logging.error(f"Error processing the file: {e}")


    def delete_files(self):
        """Delete files listed in the cleaned file"""
        from collections import defaultdict
        dir_files = defaultdict(list)
        with open(self.cleaned_file_path, "r") as f:
            for line in f:
                file_path = line.strip()
                dir_path = os.path.dirname(file_path)
                dir_files[dir_path].append(file_path)

        for dir_path, files_in_list in dir_files.items():
            try:
                system_files = [
                    os.path.join(dir_path, f)
                    for f in os.listdir(dir_path)
                    if f.endswith(".json")
                ]
            except FileNotFoundError:
                continue

            if set(system_files) == set(files_in_list):
                try:
                    for f in system_files:
                        os.remove(f)
                    os.rmdir(dir_path)
                    logging.info(f"Directory deleted: {dir_path}")
                except Exception as e:
                    logging.error(f"Error deleting directory {dir_path}: {e}")
            else:
                for f in files_in_list:
                    if os.path.exists(f):
                        try:
                            os.remove(f)
                            logging.info(f"File deleted: {f}")
                        except Exception as e:
                            logging.error(f"Error deleting file {f}: {e}")

    def process(self):
        """Execute process"""
        self.create_data()
        self.delete_files()