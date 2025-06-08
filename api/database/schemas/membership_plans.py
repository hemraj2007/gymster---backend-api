from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class DurationEnum(str, Enum):
    Monthly = "Monthly"
    Half_Yearly = "Half Yearly"
    Yearly = "Yearly"

class StatusEnum(str, Enum):
    Yes = "Yes"
    No = "No"

class MembershipPlanBase(BaseModel):
    name: str
    price: float
    duration: DurationEnum
    status: StatusEnum
    final_price: Optional[float] = None
    discount: Optional[float] = None

class MembershipPlanCreate(MembershipPlanBase):
    pass

class MembershipPlanUpdate(MembershipPlanBase):
    pass

class MembershipPlanOut(MembershipPlanBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
