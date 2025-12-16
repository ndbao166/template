from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import app_config, settings


def setup_app() -> None:
    from loguru import logger
    from rich.pretty import pretty_repr

    logger.info(f"🚀 App has been started: http://{settings.HOST}:{settings.PORT}")
    logger.info(f"🚀 OpenAPI docs: http://{settings.HOST}:{settings.PORT}/docs")
    logger.info(f"🚀 Config from {settings.CONFIG_PATH} loaded successfully: {pretty_repr(app_config)}")


def clean_app() -> None:
    pass


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    setup_app()
    yield
    clean_app()


__all__ = ["lifespan"]
