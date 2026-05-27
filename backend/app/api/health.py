from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db import get_db


router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    """Liveness check — confirms the API process is up."""
    return {"status": "ok"}


@router.get("/health/db")
def health_db(db: Session = Depends(get_db)) -> dict[str, str]:
    """Readiness check — confirms the database is reachable."""
    db.execute(text("SELECT 1"))
    return {"status": "ok"}
