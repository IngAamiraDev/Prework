import boto3
from src.scan_table import scan_dynamodb_table, save_to_csv

TABLE_NAME = 'nu4930001-sofy-bancoagricola-dev-sessions'
PROFILE_NAME = "info-dev-write-dy"
CONFIG_FILE = 'config/config.json'
PATH_DATA = 'temp/dynamodb'

items = scan_dynamodb_table(TABLE_NAME, CONFIG_FILE)
save_to_csv(items, TABLE_NAME, PATH_DATA)