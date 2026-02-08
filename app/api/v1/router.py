from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.deps import get_db

router = APIRouter()

@router.get("/ping")
def ping() -> dict:
    return {"ping": "pong"}

@router.get("/db-ping")
def db_ping(db: Session = Depends(get_db)) -> dict:
    db.execute(text("SELECT 1"))
    return {"db": "ok"}
