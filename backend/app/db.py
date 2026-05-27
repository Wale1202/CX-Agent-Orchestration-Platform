from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings


engine = create_engine(settings.database_url, pool_pre_ping=True, future=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


class Base(DeclarativeBase):
    """Base class for all ORM models."""


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency that yields a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """Create any missing tables.

    This is a dev-time convenience. In production we'd use Alembic migrations
    so schema changes are explicit and reversible. For an MVP where the
    schema is still settling, ``create_all`` is faster to iterate on.
    """
    # Import the models package so every model is registered on Base.metadata
    # before we ask SQLAlchemy to create tables.
    import app.models  # noqa: F401

    Base.metadata.create_all(bind=engine)
