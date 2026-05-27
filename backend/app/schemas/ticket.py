from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.enums import TicketCategory, TicketPriority, TicketStatus


class TicketCreate(BaseModel):
    conversation_id: int
    customer_id: int
    category: TicketCategory = "other"
    priority: TicketPriority = "medium"
    summary: str
    escalation_reason: str | None = None


class TicketUpdate(BaseModel):
    """Partial update — only the fields a human agent typically changes."""

    status: TicketStatus | None = None
    priority: TicketPriority | None = None


class TicketRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    conversation_id: int
    customer_id: int
    category: TicketCategory
    priority: TicketPriority
    status: TicketStatus
    summary: str
    escalation_reason: str | None
    created_at: datetime
    updated_at: datetime
