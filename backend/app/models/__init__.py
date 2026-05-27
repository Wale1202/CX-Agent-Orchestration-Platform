"""ORM models for the CX Agent Orchestration Platform.

Importing from this package registers every model on the shared
``Base.metadata`` so ``init_db()`` can create all tables in one call.
"""

from app.models.customer import Customer
from app.models.order import Order
from app.models.conversation import Conversation
from app.models.message import Message
from app.models.ticket import Ticket
from app.models.knowledge import KnowledgeBaseArticle

__all__ = [
    "Customer",
    "Order",
    "Conversation",
    "Message",
    "Ticket",
    "KnowledgeBaseArticle",
]
