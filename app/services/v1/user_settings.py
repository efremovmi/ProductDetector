from fastapi import status
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import select

from app.exc import raise_with_log
from app.models.auth import UserModel
from app.schemas.auth import UserSchema
from app.services.v1.base import BaseDataManager, BaseService
from app.schemas.user_settings import UserSettingsSchema
from app.models.user_settings import UserSettingsModel
from app.services.v1.auth import AuthDataManager


class UserSettingsService(BaseService):
    """User Settings service."""

    def get_settings(self, user: UserSchema) -> UserSettingsSchema:
        """Get user settings from database."""

        return UserSettingsManager(self.session).get_settings(user.email)

    def update_settings(self, user: UserSchema, user_settings: UserSettingsSchema) -> None:
        """Update user settings from database."""

        user_with_id = AuthDataManager(self.session).get_user(user.email)

        return UserSettingsManager(self.session).update_settings(user_with_id.user_id, user_settings)


class UserSettingsManager(BaseDataManager):
    def get_settings(self, email: str) -> UserSettingsSchema:
        """Read user settings from database."""

        model = self.get_one(select(UserSettingsModel).where(UserSettingsModel.user_id ==
                                                             select(UserModel.user_id).where(
                                                                 UserModel.email == email).as_scalar()))

        if not isinstance(model, UserSettingsModel):
            raise_with_log(status.HTTP_404_NOT_FOUND, "User settings not found")

        if model.settings["thresholds"] is None:
            raise_with_log(status.HTTP_500_INTERNAL_SERVER_ERROR, "Error when extracting settings")

        return UserSettingsSchema(thresholds=model.settings["thresholds"])

    def update_settings(self, user_id: int, user_settings: UserSettingsSchema) -> None:
        """Read user settings from database."""

        a = user_settings.to_dict()
        insert_stmt = insert(UserSettingsModel).values(user_id=user_id, settings=a)

        do_update_stmt = insert_stmt.on_conflict_do_update(
            index_elements=['user_id'],
            set_={'settings': a}
        )

        self.update_one(do_update_stmt)
