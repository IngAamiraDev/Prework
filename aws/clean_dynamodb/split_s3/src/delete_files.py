import sys
import json
from pathlib import Path

class DeleteFiles:
    """Separate files by date"""

    def __init__(self,
                 path_data,
                 channel_name):
        self.path_data = path_data
        self.channel_name = channel_name

    def process(self):
        """Send to delete queue"""
        dy_path = f"{self.path_data}/dynamodb/{self.channel_name}"
        file_path_to_delete = "names_processed.delete"
        full_path = f"{dy_path}/{file_path_to_delete}"
        print("Delete Files...")
        if Path(full_path).exists():
            with open(full_path, encoding="utf-8") as file:
                names_processed = json.load(file)
            print(f"Se van a borrar {len(names_processed)} archivos")
            for filename in names_processed:
                filename_path = Path(filename)
                if filename_path.is_file():
                    print("Eliminado archivo: ", filename)
                    if filename_path.stat().st_size == 0:
                        print(f"Error elimiando archivo {filename} "
                              "Por favor revisar")
                        sys.exit(1)
                    filename_path.unlink(missing_ok=True)
            Path(full_path).unlink()