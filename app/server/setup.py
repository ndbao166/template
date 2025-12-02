from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings


def setup_app() -> None:
    pass


def clean_app() -> None:
    pass


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    from loguru import logger

    setup_app()
    logger.info(f"🚀 App has been started: http://{settings.HOST}:{settings.PORT}")
    logger.info(f"🚀 OpenAPI docs: http://{settings.HOST}:{settings.PORT}/docs")
    yield
    clean_app()


__all__ = ["lifespan"]
