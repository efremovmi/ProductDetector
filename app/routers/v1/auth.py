from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.backend.session import create_session
from app.schemas.auth import TokenSchema
from app.services.v1.auth import AuthService


router = APIRouter(
    prefix="/v1",
    tags=['authentication'],
)


@router.post("/token", response_model=TokenSchema)
async def authenticate(
    login: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(create_session),
) -> TokenSchema | None:
    """User authentication.

    Raises:
        HTTPException: 401 Unauthorized
        HTTPException: 404 Not Found

    Returns:
        Access token.
    """

    return AuthService(session).authenticate(login)
