from ultralytics import YOLO
from typing import Dict
from PIL import Image
from app.const import PATH_TO_MODEL, THRESHOLD
from app.backend.config import config


class ProductDetector:
    def __init__(self):
        self.model = YOLO(config.get(PATH_TO_MODEL))
        self.threshold = config.get(THRESHOLD)

    def predict(self, image: Image) -> Dict[str, int]:
        return self.model.predict(image,  save=True, project="results", conf=self.threshold)


product_detector = ProductDetector()
