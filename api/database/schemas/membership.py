from pydantic import BaseModel
from datetime import date
from typing import Optional
from enum import Enum

class PaymentStatusEnum(str, Enum):
    paid = "paid"
    failed = "failed"
    pending = "pending"

class MembershipBase(BaseModel):
    user_id: int
    membership_id: int
    start_date: date
    expiry_date: date
    subtotal: float
    discount: float
    total: float
    promocode: Optional[str] = None
    payment_status: PaymentStatusEnum

class MembershipCreate(MembershipBase):
    pass

class MembershipUpdate(BaseModel):
    payment_status: Optional[PaymentStatusEnum] = None

class MembershipResponse(MembershipBase):
    id: int

    class Config:
        from_attributes=True
