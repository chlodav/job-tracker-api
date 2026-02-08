from fastapi import FastAPI

from app.api.v1.router import router as v1_router
from app.db.session import engine
from app.models import application, user  # noqa: F401
from app.db.base import Base

app = FastAPI(title="Job Tracker API", version="0.1.0")

app.include_router(v1_router, prefix="/api/v1")


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
