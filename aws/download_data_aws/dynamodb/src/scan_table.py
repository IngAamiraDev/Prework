import boto3
from botocore.exceptions import ClientError
import json
import csv
import os

class ScanDynamoDBTable:
    def __init__(self, table_name, config_file):
        self.table_name = table_name
        self.config_file = config_file
        self.dynamodb = None

def load_aws_credentials(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
        aws_config = config.get("aws", {})
        return aws_config.get("aws_access_key_id").strip(), \
               aws_config.get("aws_secret_access_key").strip(), \
               aws_config.get("aws_session_token").strip(), \
               aws_config.get("aws_region").strip()

def scan_dynamodb_table(table_name, config_file):
    # Load AWS credentials from config file
    aws_access_key_id, aws_secret_access_key, aws_session_token, aws_region = load_aws_credentials(config_file)

    # Configure AWS credentials
    boto3.setup_default_session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
        region_name=aws_region
    )

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    items = []
    last_evaluated_key = None

    try:
        while True:
            if last_evaluated_key:
                response = table.scan(ExclusiveStartKey=last_evaluated_key)
            else:
                response = table.scan()

            items.extend(response['Items'])
            last_evaluated_key = response.get('LastEvaluatedKey')

            if not last_evaluated_key:
                break

        return items
    except ClientError as e:
        print(f"Error scanning table {table_name}: {e.response['Error']['Message']}")
        return None

def save_to_csv(data, table_name, path_data):
    if not data:
        print("No data to save.")
        return

    # Ensure the temp directory exists
    os.makedirs(f'{path_data}/', exist_ok=True)

    # Define the CSV file path
    csv_file_path = f'{path_data}/{table_name}.csv'
    
    # Collect all unique headers from the data
    headers = set()
    for item in data:
        headers.update(item.keys())
    headers = list(headers)

    # Write data to CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved to {csv_file_path}")