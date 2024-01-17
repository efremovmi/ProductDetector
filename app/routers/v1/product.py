from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi import UploadFile, File

from app.schemas.product import ProductSchema
from app.services.v1.product import ProductService
from app.services.v1.auth import get_current_user
from app.models.image_with_products import ImageWithProducts
from app.backend.session import create_session
from app.schemas.auth import UserSchema


router = APIRouter(
    prefix="/v1",
    tags=['product'],
)


@router.post("/products_detection_to_json", response_model=List[ProductSchema])
async def get_products(file: UploadFile = File(...),
                       user: UserSchema = Depends(get_current_user),
                       session: Session = Depends(create_session),
                       ) -> List[ProductSchema]:
    request_object_content = await file.read()

    return ProductService(session).get_products(ImageWithProducts(request_object_content).get(), user)
