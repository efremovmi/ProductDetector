from pydantic import BaseModel, field_validator


class ThresholdsSchema(BaseModel):
    carrot: int
    apple: int
    onion: int
    egg: int
    limon: int

    @field_validator("carrot")
    def validate_amount_carrot(cls, value: int) -> int:
        if value < 0:
            raise ValueError("the amount of carrots should not be negative")
        return value

    @field_validator("apple")
    def validate_apple_carrot(cls, value: int) -> int:
        if value < 0:
            raise ValueError("the amount of apples should not be negative")
        return value

    @field_validator("onion")
    def validate_amount_onion(cls, value: int) -> int:
        if value < 0:
            raise ValueError("the amount of onions should not be negative")
        return value

    @field_validator("egg")
    def validate_amount_egg(cls, value: int) -> int:
        if value < 0:
            raise ValueError("the amount of eggs should not be negative")
        return value

    @field_validator("limon")
    def validate_amount_limon(cls, value: int) -> int:
        if value < 0:
            raise ValueError("the amount of limons should not be negative")
        return value


class UserSettingsSchema(BaseModel):
    thresholds: ThresholdsSchema

    @field_validator("thresholds")
    def validate_thresholds(cls, value: int) -> int:
        if value is None:
            raise ValueError("the thresholds should not be None")
        return value

    def to_dict(self):
        return {
                'thresholds': {
                    'carrot': self.thresholds.carrot,
                    'apple': self.thresholds.apple,
                    'onion': self.thresholds.onion,
                    'egg': self.thresholds.egg,
                    'limon': self.thresholds.limon,
                }
            }
