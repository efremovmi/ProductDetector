from typing import List

from app.schemas.product import ProductSchema
from app.services.v1.base import BaseDataManager, BaseService
from app.services.v1.detector import product_detector


class ProductService(BaseService):
    @staticmethod
    def get_products(path_to_image: str) -> List[ProductSchema]:
        results = product_detector.predict(path_to_image)
        result = results[0]

        product_dict = {}
        for name in result.names.values():
            product_dict[name] = 0

        for box in result.boxes:
            name = result.names[int(box.cls[0].item())]
            product_dict[name] = product_dict[name] + 1

        res = []
        for key, value in product_dict.items():
            res.append(ProductSchema(**{
                'name': key,
                'count': value,
                'is_full': value > 0,
            }))

        return res

    # def set_products_limit(self, year: int, rating: float) -> List[MovieSchema]:
    #     return MovieDataManager(self.session).get_movies(year, rating)

# class ProductDataManager(BaseDataManager):
#     def get_movie(self, movie_id: int) -> MovieSchema:
#         stmt = select(MovieModel).where(MovieModel.movie_id == movie_id)
#         model = self.get_one(stmt)
#
#         return MovieSchema(**model.to_dict())
#
#     def get_movies(self, year: int, rating: float) -> List[MovieSchema]:
#         schemas: List[MovieSchema] = list()
#
#         stmt = select(MovieModel).where(
#             MovieModel.released >= year,
#             MovieModel.rating >= rating,
#         )
#
#         for model in self.get_all(stmt):
#             schemas += [MovieSchema(**model.to_dict())]
#
#         return schemas
