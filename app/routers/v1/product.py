from typing import List

from fastapi import APIRouter
from fastapi import UploadFile, File

from app.schemas.product import ProductSchema
from app.services.v1.product import ProductService
from app.models.image_with_products import ImageWithProducts

router = APIRouter(
    prefix="/v1",
    tags=['product'],
)


@router.post("/products_detection_to_json", response_model=List[ProductSchema])
async def get_products(file: UploadFile = File(...)) -> List[ProductSchema]:
    request_object_content = await file.read()
    return ProductService().get_products(ImageWithProducts(request_object_content).get())

#
#
# @router.get("/new", response_model=List[MovieSchema])
# async def get_new_movies(
#     year: int, rating: float, session: Session = Depends(create_session)
# ) -> List[MovieSchema]:
#     return MovieService(session).get_new_movies(year, rating)
