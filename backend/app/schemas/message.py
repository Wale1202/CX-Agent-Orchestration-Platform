from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.enums import SenderType


class MessageCreate(BaseModel):
    """Payload for posting a new customer message to a conversation.

    ``sender_type`` defaults to ``"customer"``: the chat endpoint is the
    customer's mouthpiece. Agent and system messages are created internally
    by the orchestrator, not via this schema.
    """

    content: str
    sender_type: SenderType = "customer"


class MessageRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    conversation_id: int
    sender_type: SenderType
    content: str
    created_at: datetime
