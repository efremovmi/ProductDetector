import json
from typing import Any

from app.const import PATH_TO_CONFIG


class Config:
    def __init__(self):
        with open(PATH_TO_CONFIG, 'r', encoding='utf-8') as f:
            self.config = json.load(f)

    def get(self, key: str) -> Any:
        return self.config.get(key)

    def update_config(self):
        with open(PATH_TO_CONFIG, 'r', encoding='utf-8') as f:
            self.config = json.load(f)


app_config = Config()
