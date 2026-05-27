from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

from app.schemas.enums import CustomerTier


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    tier: CustomerTier = "free"


class CustomerRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    tier: CustomerTier
    created_at: datetime
