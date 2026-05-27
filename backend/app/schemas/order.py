from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from app.schemas.enums import OrderStatus


class OrderCreate(BaseModel):
    customer_id: int
    order_reference: str
    status: OrderStatus = "pending"
    total_amount: Decimal


class OrderRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    customer_id: int
    order_reference: str
    status: OrderStatus
    total_amount: Decimal
    created_at: datetime
