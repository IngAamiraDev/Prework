import os
import time
from src.clean_file import CleanFile

#PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_DATA = "temp/s3/data"
FILE_NAME = "upload_s3.txt"
FILE_DELETE = "temp/s3/upload"
CLEANED_FILE_PATH = "temp/s3/data/cleaned_upload_s3.txt"
UPLOAD_FILE = f"{FILE_DATA}/{FILE_NAME}"
#CLEANED_FILE_PATH = os.path.join(PROJECT_ROOT, "temp/s3/data/cleaned_upload_s3.txt")
#FILE_DELETE = os.path.join(PROJECT_ROOT, "temp/s3/upload")
#UPLOAD_FILE = os.path.join(PROJECT_ROOT, FILE_DATA, FILE_NAME)

start_time = time.time()
clean_file = CleanFile(FILE_DELETE, UPLOAD_FILE, CLEANED_FILE_PATH)
clean_file.process()
elapsed_time = time.time() - start_time
formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print(f"Elapsed time: {formatted_time}")