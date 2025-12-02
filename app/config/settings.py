from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PORT: int
    HOST: str
    CONFIG_PATH: str

    class Config:
        env_file = ".env"


settings = Settings()
