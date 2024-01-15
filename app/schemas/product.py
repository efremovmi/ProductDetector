from pydantic import BaseModel, field_validator

class ProductSchema(BaseModel):
    count: int
    name: str
    is_full: bool

    @field_validator("count")
    def validate_count(cls, value: int) -> int:
        if value < 0:
            raise ValueError("User must be adult")
        return value

    @field_validator("name")
    def validate_name(cls, value: str) -> str:
        if len(value) == 0:
            raise ValueError("User must be adult")
        return value
