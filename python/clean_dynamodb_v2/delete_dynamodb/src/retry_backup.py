import os
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from botocore.exceptions import ClientError, BotoCoreError

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class RetryDynamoDB:
    """reintentos de backup de dynamodb"""
    def __init__(self,
                 table_name,
                 path_data,
                 threads_num,
                 session):
        self.table = session.resource("dynamodb").Table(table_name)
        self.path_data = path_data
        self.event_num = 0
        self.threads_num = threads_num
        self.deleted_items = []

    def process(self):
        """Send to delete keys from dynamodb"""
        deleted_keys = []
        logging.info("Reading files")
        for filename in os.listdir(self.path_data):
            if filename.endswith(".json"):
                with open(os.path.join(self.path_data, filename),
                          "r",
                          encoding="utf-8") as file:
                    deleted_keys.extend(json.load(file))
        logging.info(f"Number of keys to remove: {len(deleted_keys)}")
        logging.info(f"Deleting items from {self.path_data}")
        if not deleted_keys:
            logging.warning("No data to delete")
            return
        chunk_size = round(len(deleted_keys) / self.threads_num)
        data_partition = split(deleted_keys, chunk_size)
        try:
            with ThreadPoolExecutor(max_workers=self.threads_num) as executor:
                for result in executor.map(self.delete, data_partition):
                    self.event_num += result
            for filename in os.listdir(self.path_data):
                if filename.endswith(".json"):
                    os.remove(os.path.join(self.path_data, filename))
        except (ClientError, BotoCoreError):
            self.event_num = len(self.deleted_items)
            with open(os.path.join(self.path_data, "processed.clean"),
                      "w",
                      encoding="utf-8") as file:
                json.dump(self.deleted_items, file)

    def delete(self, data):
        """Write queue to s3"""
        event_num = 0
        with self.table.batch_writer() as batch:
            for item in data:
                try:
                    batch.delete_item(Key=item)
                    event_num += 1
                    self.deleted_items.append(item)
                except ClientError as error:
                    error_code = error.response["Error"]["Code"]
                    logging.warning(
                        f"Error deleting items: {error.response['Error']['Message']}"
                    )
                    if error_code == "ExpiredTokenException":
                        raise error
        return event_num

def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]
