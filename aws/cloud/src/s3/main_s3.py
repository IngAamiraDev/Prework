import boto3
import os
import json

def load_aws_credentials(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
        aws_config = config.get("aws", {})
        return aws_config.get("aws_access_key_id").strip(), \
               aws_config.get("aws_secret_access_key").strip(), \
               aws_config.get("aws_session_token").strip(), \
               aws_config.get("aws_region").strip()

def download_all_from_s3(bucket_name, prefix, local_dir, config_file='config/config.json'):
    aws_access_key_id, aws_secret_access_key, aws_session_token, aws_region = load_aws_credentials(config_file)

    boto3.setup_default_session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
        region_name=aws_region
    )

    s3 = boto3.client('s3')

    os.makedirs(local_dir, exist_ok=True)

    try:
        paginator = s3.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
            for obj in page.get('Contents', []):
                key = obj['Key']
                local_file_path = os.path.join(local_dir, key[len(prefix):])
                local_file_dir = os.path.dirname(local_file_path)
                os.makedirs(local_file_dir, exist_ok=True)
                s3.download_file(bucket_name, key, local_file_path)
                print(f"File downloaded from S3 bucket {bucket_name} to {local_file_path}")
    except Exception as e:
        print(f"Error downloading files from S3: {e}")

bucket_name = 'nu6310001-tabot-bam-events'
prefix = 'whatsapp/unprocessed/'
local_dir = f'./exports/{bucket_name}/whatsapp/unprocessed/'

download_all_from_s3(bucket_name, prefix, local_dir)