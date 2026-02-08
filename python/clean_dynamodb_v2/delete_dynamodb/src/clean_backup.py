import os
import json
import uuid


class CleanBackup:
    """Clean backup files"""

    def __init__(self, path_data):
        self.path_data = path_data

    def process(self):
        """Send to delete queue"""
        deleted_keys = []
        deleted_file = []
        print("Reading processed keys")
        if not os.path.exists(f"{self.path_data}/processed.clean"):
            return
        with open(os.path.join(self.path_data, "processed.clean"),
                  "r",
                  encoding="utf-8") as file:
            processed_key = json.load(file)
        if not processed_key:
            return
        print("Reading deleted keys")
        for filename in os.listdir(self.path_data):
            if filename.endswith(".json"):
                with open(os.path.join(self.path_data, filename),
                          "r",
                          encoding="utf-8") as file:
                    deleted_keys.extend(json.load(file))
                    deleted_file.append(filename)
        print("Cleaning deleted keys")
        set_processed = {json.dumps(key) for key in processed_key}
        set_to_deleted = {json.dumps(key) for key in deleted_keys}
        new_to_deleted = set_to_deleted - set_processed
        lst_new_to_deleted = [json.loads(i) for i in new_to_deleted]
        print("Writing new deleted keys")
        with open(os.path.join(self.path_data, f"{uuid.uuid4()}.json"), "w",
                  encoding="utf-8") as file:
            json.dump(lst_new_to_deleted, file)
        print("Removing files")
        os.remove(os.path.join(self.path_data, "processed.clean"))
        for filename in deleted_file:
            os.remove(os.path.join(self.path_data, filename))
