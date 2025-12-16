from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PORT: int
    HOST: str
    CONFIG_PATH: str

    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_USERNAME: str
    MONGODB_PASSWORD: str
    MONGODB_DATABASE: str

    REDIS_URL_MESSAGE_BROKER: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
