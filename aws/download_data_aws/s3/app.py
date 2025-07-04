from src.download_s3 import download_all_from_s3

bucket_name = 'nu6310001-tabot-bam-dev-events'
channel = 'whatsapp'
prefix = f'{channel}/unprocessed/'
local_dir = f'temp/s3/{bucket_name}/{prefix}'
config_file='config/config.json'

download_all_from_s3(bucket_name, prefix, local_dir, config_file)