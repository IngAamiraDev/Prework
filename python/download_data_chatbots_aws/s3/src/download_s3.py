import boto3
import json
import logging
from botocore.exceptions import BotoCoreError, ClientError
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(message)s"
)

def load_aws_credentials(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
        aws_config = config.get("aws", {})
        required_keys = ["aws_access_key_id", "aws_secret_access_key", "aws_session_token", "aws_region"]
        for key in required_keys:
            if not aws_config.get(key):
                raise ValueError(f"Missing AWS config key: {key}")
        return (
            aws_config["aws_access_key_id"].strip(),
            aws_config["aws_secret_access_key"].strip(),
            aws_config["aws_session_token"].strip(),
            aws_config["aws_region"].strip()
        )

def download_all_from_s3(bucket_name, prefix, local_dir, config_file, overwrite=False):
    """
    Downloads all files from an S3 bucket under a given prefix.
    Args:
        bucket_name (str): Name of the bucket.
        prefix (str): Prefix of the files to download.
        local_dir (str): Local directory to save the files.
        config_file (str): Path to the configuration file.
        overwrite (bool): If True, overwrite existing files.
    """
    try:
        aws_access_key_id, aws_secret_access_key, aws_session_token, aws_region = load_aws_credentials(config_file)
    except Exception as e:
        logging.error(f"Error loading credentials: {e}")
        return

    boto3.setup_default_session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
        region_name=aws_region
    )

    s3 = boto3.client('s3')
    Path(local_dir).mkdir(parents=True, exist_ok=True)

    try:
        paginator = s3.get_paginator('list_objects_v2')
        total = 0
        for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
            for obj in page.get('Contents', []):
                key = obj['Key']
                local_file_path = Path(local_dir) / (key[len(prefix):] + ".csv")
                local_file_path.parent.mkdir(parents=True, exist_ok=True)
                if not overwrite and local_file_path.exists():
                    logging.info(f"File already exists, skipping: {local_file_path}")
                    continue
                try:
                    s3.download_file(bucket_name, key, str(local_file_path))
                    logging.info(f"Downloaded: {local_file_path}")
                    total += 1
                except (BotoCoreError, ClientError) as e:
                    logging.error(f"Error downloading {key}: {e}")
        logging.info(f"Total files downloaded: {total}")
    except Exception as e:
        logging.error(f"General error downloading files from S3: {e}")