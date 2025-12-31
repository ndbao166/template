import hashlib
from datetime import datetime, timedelta
from typing import Annotated, Any

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from app.config import settings
from app.database.model import User
from app.exception import EmailAlreadyRegisteredError, UsernameAlreadyRegisteredError
from app.server.repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        result: bool = hashlib.sha256(plain_password.encode()).hexdigest() == hashed_password
        return result

    def get_password_hash(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    async def authenticate_user(self, username: str, password: str) -> User | None:
        user = await self.user_repository.get_user_by_username_with_hashed_password(username)
        if not user:
            return None
        if not self.verify_password(password, user.hashed_password):
            return None
        return User(**user.model_dump())

    def create_access_token(self, data: dict[str, str], expires_delta: timedelta | None = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode_with_exp: dict[str, Any] = {**to_encode, "exp": expire}
        encoded_jwt: str = jwt.encode(to_encode_with_exp, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt

    async def register_user(self, email: str, username: str, password: str) -> User:
        try:
            existing_user = await self.user_repository.get_by_email(email)
            if existing_user:
                raise EmailAlreadyRegisteredError(email)

            existing_user = await self.user_repository.get_by_username(username)
            if existing_user:
                raise UsernameAlreadyRegisteredError(username)

            user_id = await self.user_repository.create_user(
                email=email,
                username=username,
                hashed_password=self.get_password_hash(password),
            )

            user = await self.user_repository.get_by_id(user_id)
            if user is None:
                raise ValueError(f"User {user_id} not found")
            return user
        except Exception as e:
            raise ValueError(f"Error registering user: {e}") from e

    async def login_user(self, username: str, password: str) -> str:
        try:
            user = await self.authenticate_user(username, password)
            if user is None:
                raise ValueError("Invalid credentials")

            access_token_expires = timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)

            access_token = self.create_access_token(
                data={"sub": str(user.id)},
                expires_delta=access_token_expires,
            )

            return access_token
        except Exception as e:
            raise ValueError(f"Error logging in user: {e}") from e

    async def get_current_user(self, token: str) -> User:
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            user_id: str | None = payload.get("sub")
            if user_id is None:
                raise ValueError("Invalid token")

            user = await self.user_repository.get_by_id(user_id)
            if user is None:
                raise ValueError("User not found")

            return user
        except Exception as e:
            raise ValueError(f"Error getting user: {e}") from e


def get_auth_service() -> AuthService:
    from app.server.repository import get_user_repository

    return AuthService(user_repository=get_user_repository())


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
) -> User:
    return await auth_service.get_current_user(token)
