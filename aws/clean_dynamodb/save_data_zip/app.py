import os
import time
import logging
from src.scan_zip import ScanS3Zip

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

PATH_DATA = "temp/s3"
CHANNEL_NAME = "cpc"
start_time = time.time()
source_dir = f"{PATH_DATA}/{CHANNEL_NAME}"
zip_prefix = f"{PATH_DATA}/{CHANNEL_NAME}"
splitter = ScanS3Zip(source_dir, zip_prefix)
splitter.process()
elapsed_time = time.time() - start_time
formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
logging.info(f"Tiempo transcurrido: {formatted_time}")