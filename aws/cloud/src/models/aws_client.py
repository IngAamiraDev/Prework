import boto3
from botocore.exceptions import ClientError


class AWSClient:

    def __init__(self, config, logger):
        aws_config = config.get("aws")
        self._service_region = aws_config.get("aws_region", None)
        _access_key = aws_config.get("aws_access_key_id", "")
        _secret_key = aws_config.get("aws_secret_access_key", "")
        _session_token = aws_config.get("aws_session_token", "")
        self._access_key = _access_key or None
        self._secret_key = _secret_key or None
        self._session_token = _session_token or None
        self.logger = logger

    def generate_authorized_client(self, service_name):
        """
        Generate an authorized aws client.
        """
        try:
            return boto3.client(service_name, region_name=self._service_region,
                                aws_access_key_id=self._access_key,
                                aws_secret_access_key=self._secret_key,
                                aws_session_token=self._session_token)
        except ClientError as e:
            error = e.response.get("Error")
            self.logger.add_error(
                f"Error at [AWS_Client][generate_authorized_client]"
                f" Detail: {error}")