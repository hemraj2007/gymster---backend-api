from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from api.database.connection import Base
import enum

# ✅ Enum class for payment status
class PaymentStatusEnum(str, enum.Enum):
    paid = "paid"
    failed = "failed"
    pending = "pending"

# ✅ Membership model
class Membership(Base):  # 🔥 Class name capital hona chahiye (Python standard)
    __tablename__ = "membership"  # 🔥 Yeh sahi syntax hai (__tablename__ not _tablename_)

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    membership_id = Column(Integer, ForeignKey("membership_plans.id"))
    start_date = Column(Date)
    expiry_date = Column(Date)
    subtotal = Column(Float)
    discount = Column(Float)
    total = Column(Float)
    promocode = Column(String(50), nullable=True)
    payment_status = Column(Enum(PaymentStatusEnum), default=PaymentStatusEnum.pending)

    # ✅ Relationships
    user = relationship("User")
    membership_plan = relationship("MembershipPlan")
