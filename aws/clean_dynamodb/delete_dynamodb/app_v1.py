import time
import boto3
from src.retry_backup import RetryDynamoDB
from src.clean_backup import CleanBackup

TABLE_NAME = "tabot-aw1165001-events-cpc"
PROFILE_NAME = "info-pdn-write-dy"
CHANNEL_NAME = "cpc"
PATH_DATA = f"temp/dynamodb/{CHANNEL_NAME}"
THREADS_NUM = 12

session = boto3.Session(profile_name=PROFILE_NAME)
start_time = time.time()
CleanBackup(PATH_DATA).process()
retry = RetryDynamoDB(TABLE_NAME, PATH_DATA, THREADS_NUM, session)
retry.process()
elapsed_time = time.time() - start_time
formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print(f"Number of events: {retry.event_num}.")
print(f"Elapsed time: {formatted_time}")
