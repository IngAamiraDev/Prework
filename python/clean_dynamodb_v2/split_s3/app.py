import os
import time
from datetime import datetime, timedelta
from src.split import SplitS3
from src.split_zip import SplitS3Zip

CHANNEL_NAME = "cpc"
#PATH_DATA = "temp"
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_DATA = os.path.join(PROJECT_ROOT, "temp")
MAX_DATE = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
MAX_EVENTS_NUM = 4500000  # +/- 18 GB Event to process
THREADS_NUM = 12

user_choice = input("Enter 1 for SplitS3 or 0 for SplitS3Zip: ").strip()

if user_choice == "1":
    start_time = time.time()
    split_s3 = SplitS3(PATH_DATA,
                       CHANNEL_NAME,
                       MAX_DATE,
                       THREADS_NUM,
                       MAX_EVENTS_NUM)
    split_s3.process()
    elapsed_time = time.time() - start_time
elif user_choice == "0":
    start_time = time.time()
    split_s3_zip = SplitS3Zip(PATH_DATA,
                              CHANNEL_NAME,
                              MAX_DATE,
                              THREADS_NUM,
                              MAX_EVENTS_NUM)
    split_s3_zip.process()
    elapsed_time = time.time() - start_time
else:
    print("Invalid choice. Please enter 1 or 0.")
    elapsed_time = None

if elapsed_time is not None:
    formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
    print(f"Elapsed time: {formatted_time}")