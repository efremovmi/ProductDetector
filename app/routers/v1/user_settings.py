from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.services.v1.user_settings import UserSettingsService
from app.services.v1.auth import get_current_user
from app.backend.session import create_session
from app.schemas.auth import UserSchema
from app.schemas.user_settings import UserSettingsSchema

router = APIRouter(
    prefix="/v1",
    tags=['user settings'],
)


@router.get("/settings", response_model=UserSettingsSchema)
async def get_settings(
        user: UserSchema = Depends(get_current_user),
        session: Session = Depends(create_session)) -> UserSettingsSchema:

    return UserSettingsService(session).get_settings(user)


@router.put("/settings")
async def update_settings(
        user_settings: UserSettingsSchema,
        user: UserSchema = Depends(get_current_user),
        session: Session = Depends(create_session)):

    UserSettingsService(session).update_settings(user, user_settings)

    return {"status": "ok"}

