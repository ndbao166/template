from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.database.model import User
from app.server.schema.request.user import RegisterUserRequest
from app.server.schema.response.user import Token
from app.server.service.auth_service import AuthService, get_auth_service, get_current_user

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: RegisterUserRequest,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
) -> User:
    return await auth_service.register_user(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password,
    )


@router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
) -> Token:
    access_token = await auth_service.login_user(
        username=form_data.username,
        password=form_data.password,
    )
    return Token(access_token=access_token)


@router.get("/me", response_model=User, status_code=status.HTTP_200_OK)
async def get_me(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    return current_user
