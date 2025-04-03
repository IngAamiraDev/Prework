# LocalStack setup script for creating and deleting AWS resources
import boto3
import os
import sys

# LocalStack endpoint, region and credentials
ENDPOINT_URL = "http://localhost:4566"
REGION = "us-east-1"
AWS_ACCESS_KEY_ID = "test"
AWS_SECRET_ACCESS_KEY = "test"

# Create boto3 clients with credentials and LocalStack endpoint
dynamodb = boto3.client(
    "dynamodb",
    region_name=REGION,
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)
s3 = boto3.client(
    "s3",
    region_name=REGION,
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)
_lambda = boto3.client(
    "lambda",
    region_name=REGION,
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

def drop_dynamodb_table():
    table_name = "artemis-local-change-registry-dy"
    try:
        existing_tables = dynamodb.list_tables()["TableNames"]
        if table_name in existing_tables:
            dynamodb.delete_table(TableName=table_name)
            waiter = dynamodb.get_waiter("table_not_exists")
            waiter.wait(TableName=table_name)
            print(f"DynamoDB table deleted: {table_name}")
    except Exception as e:
        print(f"Error deleting DynamoDB table {table_name}: {e}")

def drop_s3_bucket(bucket):
    try:
        # Verify the bucket exists
        s3.head_bucket(Bucket=bucket)
        # Delete all objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket).get("Contents", [])
        for obj in objects:
            s3.delete_object(Bucket=bucket, Key=obj["Key"])
        s3.delete_bucket(Bucket=bucket)
        print(f"S3 bucket deleted: {bucket}")
    except Exception as e:
        print(f"Error deleting bucket {bucket}: {e}")

def drop_all_s3_buckets():
    buckets = [
        "artemis-local-versioned-pickle",
        "artemis-multimedia-local",
        "sofy-multimedia-local",
        "tabot-multimedia-local",
        "artemis-local-prototypes",
    ]
    for bucket in buckets:
        drop_s3_bucket(bucket)

def drop_lambda_function():
    function_name = "copy_skills_lambda"
    try:
        _lambda.get_function(FunctionName=function_name)
        _lambda.delete_function(FunctionName=function_name)
        print(f"Lambda function deleted: {function_name}")
    except _lambda.exceptions.ResourceNotFoundException:
        print(f"Lambda function does not exist: {function_name}")
    except Exception as e:
        print(f"Error deleting Lambda function {function_name}: {e}")

def create_dynamodb_table():
    table_name = "artemis-local-change-registry-dy"
    try:
        dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {"AttributeName": "registry_id", "KeyType": "HASH"},
                {"AttributeName": "promoter_datetime", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "registry_id", "AttributeType": "S"},
                {"AttributeName": "promoter_datetime", "AttributeType": "S"},
            ],
            BillingMode="PAY_PER_REQUEST",
        )
        print(f"DynamoDB table created: {table_name}")
        waiter = dynamodb.get_waiter("table_exists")
        waiter.wait(TableName=table_name)
    except Exception as e:
        print(f"Error creating DynamoDB table {table_name}: {e}")

def create_s3_buckets():
    buckets = [
        "artemis-local-versioned-pickle",
        "artemis-multimedia-local",
        "sofy-multimedia-local",
        "tabot-multimedia-local",
        "artemis-local-prototypes",
    ]
    for bucket in buckets:
        try:
            s3.create_bucket(Bucket=bucket)
            print(f"S3 bucket created: {bucket}")
        except Exception as e:
            print(f"Error creating bucket {bucket}: {e}")

def create_s3_folders():
    channels = ["teams", "webchat", "whatsapp"]
    bucket = "sofy-multimedia-local"
    for channel in channels:
        key = f"{channel}/image/"
        try:
            s3.put_object(Bucket=bucket, Key=key)
            print(f"Folder created in bucket {bucket}: {key}")
        except Exception as e:
            print(f"Error creating folder {key}: {e}")

def upload_files_to_s3():
    bucket = "sofy-multimedia-local"
    local_files = [
        "/mnt/c/amira/Bancolombia/Local-Stack/imgs/N-00-00-01.png",
        "/mnt/c/amira/Bancolombia/Local-Stack/imgs/N-00-00-02.png",
        "/mnt/c/amira/Bancolombia/Local-Stack/imgs/N-00-00-03.png",
    ]
    channels = ["teams", "webchat", "whatsapp"]
    for local_file in local_files:
        if not os.path.exists(local_file):
            sys.exit(f"File not found: {local_file}. Check the file path and try again.")
        for channel in channels:
            key = f"{channel}/image/{os.path.basename(local_file)}"
            try:
                s3.upload_file(local_file, bucket, key)
                print(f"Uploaded file to {bucket}: {key}")
            except s3.exceptions.ClientError as error:
                print(f"Error uploading {local_file} to {key}: {error}")

def create_lambda_function():
    zip_file_path = "/mnt/c/amira/Bancolombia/Sprints/214/copy_skills_lambda.zip"
    function_name = "copy_skills_lambda"
    try:
        with open(zip_file_path, "rb") as f:
            zipped_code = f.read()
        _lambda.create_function(
            FunctionName=function_name,
            Runtime="python3.8",
            Role="arn:aws:iam::000000000000:role/execution_role",
            Handler="lambda_function.lambda_handler",
            Code={"ZipFile": zipped_code},
            Publish=True,
        )
        print(f"Lambda function created: {function_name}")
    except Exception as e:
        print(f"Error creating Lambda function {function_name}: {e}")

if __name__ == "__main__":
    # Delete existing resources if they exist
    #drop_dynamodb_table()
    #drop_all_s3_buckets()
    #drop_lambda_function()

    # Create resources
    #create_dynamodb_table()
    #create_s3_buckets()
    #create_s3_folders()
    #create_lambda_function()

    # Upload resources   
    upload_files_to_s3()