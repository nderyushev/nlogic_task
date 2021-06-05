import os
from typing import BinaryIO

import requests
from loguru import logger


class Uploader:
    API_URL = "http://localhost/images"
    VALID_FORMATS = ("*.jpg", "*.png", "*.gif")

    def __init__(self, dir_path: str):
        self.dir_path = dir_path

    def upload(self):
        images = self._pick_images()

        for image in images:
            with open(f'{self.dir_path}/{image}', "rb") as f:
                self._upload_request(f)

    def _pick_images(self) -> list[str]:
        files = os.listdir(self.dir_path)

        return list(
            filter(lambda f: os.path.splitext(f)[1] not in self.VALID_FORMATS, files)
        )

    def _upload_request(self, file) -> None:
        response = requests.post(self.API_URL, files={'image': file})
        logger.info(response.text)
