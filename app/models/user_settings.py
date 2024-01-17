from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON

from app.models.base import SQLModel


class UserSettingsModel(SQLModel):
    __tablename__ = "users_settings"
    __table_args__ = {"schema": "public"}

    id:       Mapped[int] = mapped_column("id", primary_key=True)
    user_id:  Mapped[int] = mapped_column("user_id")
    settings: Mapped[dict] = mapped_column("settings", type_=JSON, nullable=False)
