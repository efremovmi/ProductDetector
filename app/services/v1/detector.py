from ultralytics import YOLO
from typing import Dict
from PIL import Image

from app.const import PATH_TO_MODEL, THRESHOLD
from app.backend.config import app_config


class ProductDetector:
    def __init__(self):
        self.model = YOLO(app_config.get(PATH_TO_MODEL))

    def predict(self, image: Image) -> Dict[str, int]:
        return self.model.predict(image,  save=True, project="results", conf=app_config.get(THRESHOLD))


product_detector = ProductDetector()
