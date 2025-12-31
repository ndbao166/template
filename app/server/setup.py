from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import app_config, settings


async def setup_app() -> None:
    from loguru import logger
    from rich.pretty import pretty_repr

    from app.database import setup_mongodb

    await setup_mongodb(
        host=settings.MONGODB_HOST,
        port=settings.MONGODB_PORT,
        username=settings.MONGODB_USERNAME,
        password=settings.MONGODB_PASSWORD,
        database_name=settings.MONGODB_DATABASE,
    )

    logger.info(f"🚀 App has been started: http://{settings.HOST}:{settings.PORT}")
    logger.info(f"🚀 OpenAPI docs: http://{settings.HOST}:{settings.PORT}/docs")
    logger.info(f"🚀 Config from {settings.CONFIG_PATH} loaded successfully: {pretty_repr(app_config)}")


def clean_app() -> None:
    from app.database import close_mongodb

    close_mongodb()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    await setup_app()
    yield
    clean_app()


__all__ = ["lifespan"]
