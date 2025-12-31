from typing import Any

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection

from app.config import settings
from app.database.model import User, UserDBModel


class UserRepository:
    def __init__(self, collection: AsyncIOMotorCollection[Any]):
        self.collection = collection

    async def get_by_id(self, user_id: str) -> User | None:
        document = await self.collection.find_one({"_id": ObjectId(user_id)})
        if document:
            return User(**document)
        return None

    async def create_user(self, email: str, username: str, hashed_password: str) -> str:
        from datetime import datetime

        user = UserDBModel(email=email, username=username, hashed_password=hashed_password, created_at=datetime.now(), is_active=True)
        result = await self.collection.insert_one(user.model_dump(by_alias=True, exclude={"id"}))
        return str(result.inserted_id)

    async def get_by_email(self, email: str) -> User | None:
        document = await self.collection.find_one({"email": email})
        if document:
            return User(**document)
        return None

    async def get_by_username(self, username: str) -> User | None:
        document = await self.collection.find_one({"username": username})
        if document:
            return User(**document)
        return None

    async def get_user_by_username_with_hashed_password(self, username: str) -> UserDBModel | None:
        document = await self.collection.find_one({"username": username})
        if document:
            return UserDBModel(**document)
        return None


def get_user_repository() -> UserRepository:
    from app.database import get_collection

    return UserRepository(collection=get_collection(settings.MONGODB_DATABASE, "users"))
