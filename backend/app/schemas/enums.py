"""Shared `Literal` aliases used by API schemas.

Kept here rather than as `enum.Enum` classes so they stay lightweight and
easy to widen. The database stores these as plain strings.
"""

from typing import Literal


CustomerTier = Literal["free", "pro", "enterprise"]

OrderStatus = Literal["pending", "shipped", "delivered", "cancelled", "refunded"]

ConversationChannel = Literal["web", "email", "chat"]
ConversationStatus = Literal["active", "escalated", "closed"]

SenderType = Literal["customer", "ai_agent", "human_agent", "system"]

Urgency = Literal["low", "medium", "high"]

TicketCategory = Literal["billing", "shipping", "technical", "account", "other"]
TicketPriority = Literal["low", "medium", "high", "urgent"]
TicketStatus = Literal["open", "in_progress", "resolved", "closed"]
