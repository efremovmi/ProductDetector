import uuid

from app.backend.config import app_config
from app.const import PATH_TO_BUFFER


class ImageWithProducts:
    def __init__(self, request_object_content: bytes):
        self.path_to_file = app_config.get(PATH_TO_BUFFER) + "/" + str(uuid.uuid4()) + ".jpg"
        with open(self.path_to_file, "wb") as buffer:
            buffer.write(request_object_content)

    def get(self) -> str:
        return self.path_to_file
