from typing import Any

import uvicorn
from fastapi import FastAPI

from app.config import settings
from app.server import lifespan

app = FastAPI(
    title="Learn FastAPI",
    description="### Learn FastAPI",
    version="0.1.0",
    lifespan=lifespan,
    dependencies=[],
)


@app.get("/")
async def root() -> str:
    return "Hello word"


@app.get("/items/{item_id}")
async def read_item(item_id: str) -> dict[str, Any]:
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
