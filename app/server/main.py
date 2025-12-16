import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.server import lifespan

app = FastAPI(
    title="Learn FastAPI",
    description="### Learn FastAPI",
    version="0.1.0",
    lifespan=lifespan,
    dependencies=[],
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vite default port and common React ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> str:
    return "Hello word"


if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
