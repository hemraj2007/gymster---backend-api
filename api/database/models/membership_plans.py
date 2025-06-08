from sqlalchemy import Column, Integer, String, Float, Enum, DateTime
from sqlalchemy.sql import func
from api.database.base import Base
import enum

class DurationEnum(str, enum.Enum):
    Monthly = "Monthly"
    Half_Yearly = "Half Yearly"
    Yearly = "Yearly"

class StatusEnum(str, enum.Enum):
    Yes = "Yes"
    No = "No"

class MembershipPlan(Base):
    __tablename__ = "membership_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    duration = Column(Enum(DurationEnum), nullable=False)
    status = Column(Enum(StatusEnum), default="Yes")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    final_price = Column(Float, nullable=True)   # nullable float
    discount = Column(Float, nullable=True)      # nullable float, changed from String to Float
    
