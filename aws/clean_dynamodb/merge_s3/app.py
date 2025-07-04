import time
from src.merge import MergeSubdir
import sys

CHANNEL_NAME = "cpc"
PATH_DATA = "temp/s3"

user_choice = input("Enter 1 to skip extracting zip files or 0 to extract zip files: ").strip()

if user_choice not in ["0", "1"]:
    print("Invalid input. Please enter 1 or 0.")
    sys.exit(1)

start_time = time.time()
merge_and_upload = MergeSubdir(CHANNEL_NAME, PATH_DATA)

if user_choice == "0":
    merge_and_upload.extract_zip_files()

merge_and_upload.merge_directories()
elapsed_time = time.time() - start_time
formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print(f"Elapsed time: {formatted_time}")