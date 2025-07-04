import boto3
import json
from botocore.exceptions import ClientError
import subprocess
import time
import sys

# AWS configuration
ENDPOINT_URL = "http://localhost:4566"
REGION = "us-east-1"
AWS_ACCESS_KEY_ID ="local-access-key"
AWS_SECRET_ACCESS_KEY ="local-secret-access-key"
AWS_SESSION_TOKEN ="local-session-token"

# This function runs a LocalStack Docker container and waits for it to be ready
def start_localstack():
    try:
        print("Starting LocalStack...")
        container_id = subprocess.check_output(
            ["docker", "run", "-d", "-p", "4566:4566", "localstack/localstack"]
        ).strip().decode("utf-8")
        time.sleep(8)
        print(f"LocalStack started with container ID: {container_id}")
        return container_id
    except Exception as e:
        print(f"Error starting LocalStack: {e}")
        sys.exit(1)

# Create boto3 clients with credentials and LocalStack endpoint
secretsmanager = boto3.client(
    "secretsmanager",
    region_name=REGION,
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
)
dynamodb = boto3.client(
    "dynamodb",
    region_name=REGION,
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
)
s3 = boto3.client(
    "s3",
    region_name=REGION,
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
)

# Delete a secret if it exists
def delete_secret(secret_name):
    try:
        secretsmanager.delete_secret(SecretId=secret_name, ForceDeleteWithoutRecovery=True)
        print(f"Secret '{secret_name}' deleted successfully.")
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            print(f"Secret '{secret_name}' does not exist.")
        else:
            print(f"Error deleting secret '{secret_name}': {e}")

# Create a secret in Secrets Manager
def create_secret():
    secret_name = "aio-db-secrests"
    secret_value = {
        "password": "mysecretpassword",
        "dbname": "postgres",
        "engine": "postgres",
        "port": 5432,
        "dbInstanceIdentifier": "llm-postgres",
        "host": "localhost",
        "username": "postgres",
    }

    delete_secret(secret_name)  # Delete the secret if it exists

    try:
        secretsmanager.create_secret(
            Name=secret_name,
            SecretString=json.dumps(secret_value),
        )
        print(f"Secret '{secret_name}' created successfully.")
    except Exception as e:
        print(f"Error creating secret '{secret_name}': {e}")

# Delete a DynamoDB table if it exists
def drop_dynamodb_table(table_name):
    try:
        dynamodb.delete_table(TableName=table_name)
        print(f"DynamoDB table '{table_name}' deleted successfully.")
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            print(f"DynamoDB table '{table_name}' does not exist.")
        else:
            print(f"Error deleting DynamoDB table '{table_name}': {e}")

# Create a DynamoDB table
def create_dynamodb_table():
    table_name = "nu0087001-aid-r2-local-dynamo-config-control"

    drop_dynamodb_table(table_name)  # Delete the table if it exists

    try:
        dynamodb.create_table(
            TableName=table_name,
            AttributeDefinitions=[
                {"AttributeName": "s3_path", "AttributeType": "S"},
            ],
            KeySchema=[
                {"AttributeName": "s3_path", "KeyType": "HASH"},
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1,
            },
        )
        print(f"DynamoDB table '{table_name}' created successfully.")
    except Exception as e:
        print(f"Error creating DynamoDB table '{table_name}': {e}")

def drop_s3_bucket(bucket):
    try:
        s3.head_bucket(Bucket=bucket)
        objects = s3.list_objects_v2(Bucket=bucket).get("Contents", [])
        for obj in objects:
            s3.delete_object(Bucket=bucket, Key=obj["Key"])
        s3.delete_bucket(Bucket=bucket)
        print(f"S3 bucket deleted: {bucket}")
    except ClientError as e:
        if e.response["Error"]["Code"] == "404":
            print(f"S3 bucket '{bucket}' does not exist.")
        else:
            print(f"Error deleting bucket '{bucket}': {e}")
    except Exception as e:
        print(f"Unexpected error deleting bucket '{bucket}': {e}")

def create_s3_buckets():
    buckets = [
        "aio-raw-bucket-testing",
    ]
    for bucket in buckets:
        drop_s3_bucket(bucket)
        try:
            s3.create_bucket(Bucket=bucket)
            print(f"S3 bucket created: {bucket}")
        except Exception as e:
            print(f"Error creating bucket '{bucket}': {e}")

if __name__ == "__main__":
    start_localstack()
    #create_secret()
    #create_dynamodb_table()
    #create_s3_buckets()