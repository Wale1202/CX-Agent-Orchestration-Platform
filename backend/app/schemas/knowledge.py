from datetime import datetime

from pydantic import BaseModel, ConfigDict


class KnowledgeBaseArticleCreate(BaseModel):
    title: str
    category: str
    content: str
    tags: list[str] = []


class KnowledgeBaseArticleRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    category: str
    content: str
    tags: list[str]
    created_at: datetime
