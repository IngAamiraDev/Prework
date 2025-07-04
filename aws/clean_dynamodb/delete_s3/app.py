import boto3

S3_NAME = "aw1165001-tabot-pdn-events"
PROFILE_NAME = "info-pdn-write-s3"
CHANNEL_NAME = "cpc"

session = boto3.Session(profile_name=PROFILE_NAME)
s3_client = session.client("s3")

files_to_delete = [f"{CHANNEL_NAME}-4.zip", f"{CHANNEL_NAME}-5.zip"]

for file_key in files_to_delete:
    try:
        s3_client.delete_object(Bucket=S3_NAME, Key=file_key)
        print(f"Deleted {file_key} from {S3_NAME}")
    except Exception as e:
        print(f"Error deleting {file_key}: {e}")