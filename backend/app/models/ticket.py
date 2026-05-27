from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Ticket(Base):
    """A support ticket opened when the agent escalates a conversation.

    Expected ``category`` values: ``"billing"``, ``"shipping"``,
    ``"technical"``, ``"account"``, ``"other"``.

    Expected ``priority`` values: ``"low"``, ``"medium"``, ``"high"``,
    ``"urgent"``.

    Expected ``status`` values: ``"open"``, ``"in_progress"``, ``"resolved"``,
    ``"closed"``.
    """

    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id", ondelete="CASCADE"), index=True
    )
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id", ondelete="CASCADE"), index=True
    )

    category: Mapped[str] = mapped_column(String(32), default="other")
    priority: Mapped[str] = mapped_column(String(16), default="medium", index=True)
    status: Mapped[str] = mapped_column(String(16), default="open", index=True)
    summary: Mapped[str] = mapped_column(String(255))
    # Why the conversation was escalated — written by the agent or a rule.
    escalation_reason: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    conversation: Mapped["Conversation"] = relationship(back_populates="tickets")
    customer: Mapped["Customer"] = relationship(back_populates="tickets")
