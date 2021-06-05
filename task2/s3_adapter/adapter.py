from typing import IO

from minio import Minio
from loguru import logger


class S3Adapter:
    def __init__(self):
        self.client = Minio(
            "s3:9000", access_key="minio", secret_key="minio123", secure=False
        )

    def push_file(self, bucket_name: str, object_name: str, file: int) -> None:
        self.create_bucket_if_not_exists(bucket_name)
        self.client.fput_object(bucket_name, object_name, file)

    def create_bucket_if_not_exists(self, bucket_name: str) -> None:
        is_found = self.client.bucket_exists(bucket_name)

        if not is_found:
            self.client.make_bucket(bucket_name)
            logger.info(f"Bucket {bucket_name} successfully created")
