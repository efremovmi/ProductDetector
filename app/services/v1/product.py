from typing import List

from app.schemas.product import ProductSchema
from app.schemas.auth import UserSchema
from app.services.v1.base import BaseService
from app.services.v1.detector import product_detector
from app.services.v1.user_settings import UserSettingsManager


class ProductService(BaseService):
    """Product Service"""

    def get_products(self, path_to_image: str, user: UserSchema) -> List[ProductSchema]:
        results = product_detector.predict(path_to_image)
        result = results[0]

        product_dict = {}
        for name in result.names.values():
            product_dict[name] = 0

        for box in result.boxes:
            name = result.names[int(box.cls[0].item())]
            product_dict[name] = product_dict[name] + 1

        settings = UserSettingsManager(self.session).get_settings(user.email)
        settings = dict(settings.thresholds)

        res = []
        for key, value in product_dict.items():
            field = settings.get(key)
            if field is None:
                field = 0

            res.append(ProductSchema(**{
                'name': key,
                'count': value,
                'is_full': value >= field,
            }))

        return res
