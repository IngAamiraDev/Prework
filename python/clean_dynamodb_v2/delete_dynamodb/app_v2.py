import shutil
import time
import boto3
import glob
import os
from src.retry_backup import RetryDynamoDB
from src.clean_backup import CleanBackup

TABLE_NAME = "tabot-aw1165001-events-cpc"
PROFILE_NAME = "info-pdn-write-dy"
CHANNEL_NAME = "cpc"
THREADS_NUM = 12

session = boto3.Session(profile_name=PROFILE_NAME)
start_time = time.time()
base_path = f"temp/dynamodb/{CHANNEL_NAME}-*"
dirs = sorted([d for d in glob.glob(base_path) if os.path.isdir(d)])

for path in dirs:
    CleanBackup(path).process()
    retry = RetryDynamoDB(TABLE_NAME, path, THREADS_NUM, session)
    retry.process()
    print(f"Number of events in {path}: {retry.event_num}.")
    shutil.rmtree(path)
    print(f"Directories processed and deleted: {dirs}")

elapsed_time = time.time() - start_time
formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print(f"Elapsed time: {formatted_time}")