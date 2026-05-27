from datetime import datetime

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class KnowledgeBaseArticle(Base):
    """A canonical support article the agent can retrieve to answer questions.

    ``tags`` is a Postgres ``text[]`` column for simple keyword filtering.
    Embeddings for semantic search will be added in a later phase (pgvector)
    and live on a separate ``knowledge_chunks`` table to keep this one small.
    """

    __tablename__ = "knowledge_base_articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    category: Mapped[str] = mapped_column(String(64), index=True)
    content: Mapped[str] = mapped_column(Text)
    tags: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
