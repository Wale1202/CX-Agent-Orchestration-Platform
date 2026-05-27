from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.enums import ConversationChannel, ConversationStatus, Urgency
from app.schemas.message import MessageRead


class ConversationCreate(BaseModel):
    customer_id: int
    channel: ConversationChannel = "web"


class ConversationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    customer_id: int
    channel: ConversationChannel
    status: ConversationStatus
    sentiment: float | None = Field(default=None, ge=-1.0, le=1.0)
    urgency: Urgency | None = None
    confidence_score: float | None = Field(default=None, ge=0.0, le=1.0)
    created_at: datetime
    updated_at: datetime


class ConversationDetail(ConversationRead):
    """Conversation with its message history. Used by the dashboard view."""

    messages: list[MessageRead] = []
