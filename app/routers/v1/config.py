from fastapi import APIRouter, Depends

from app.backend.config import app_config
from app.services.v1.auth import get_current_user
from app.schemas.auth import UserSchema

router = APIRouter(
    prefix="/v1",
    tags=['config'],
)


@router.post("/update", status_code=200)
async def config_update(_: UserSchema = Depends(get_current_user)) -> dict[str, str]:
    app_config.update_config()
    return {"status": "ok"}
