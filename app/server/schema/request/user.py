from pydantic import BaseModel, EmailStr


class RegisterUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginUserRequest(BaseModel):
    username: str
    password: str
