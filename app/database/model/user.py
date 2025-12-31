from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, BeforeValidator, ConfigDict, EmailStr, Field

PyObjectId = Annotated[str, BeforeValidator(str)]


class User(BaseModel):
    id: PyObjectId | None = Field(validation_alias="_id", default=None)
    username: str
    email: EmailStr
    created_at: datetime
    is_active: bool

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class UserDBModel(User):
    hashed_password: str
