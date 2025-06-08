from sqlalchemy.orm import Session
from api.database.models import  membership as models
from api.database.schemas import membership as schemas

def create_membership(db: Session, membership: schemas.MembershipCreate):
    db_membership = models.Membership(**membership.dict())
    db.add(db_membership)
    db.commit()
    db.refresh(db_membership)
    return db_membership

def get_all_memberships(db: Session):
    return db.query(models.Membership).all()

def get_membership_by_id(db: Session, membership_id: int):
    return db.query(models.Membership).filter(models.Membership.id == membership_id).first()

def update_membership_status(db: Session, membership_id: int, status: schemas.PaymentStatusEnum):
    db_membership = get_membership_by_id(db, membership_id)
    if db_membership:
        db_membership.payment_status = status
        db.commit()
        db.refresh(db_membership)
    return db_membership

def delete_membership(db: Session, membership_id: int):
    db_membership = get_membership_by_id(db, membership_id)
    if db_membership:
        db.delete(db_membership)
        db.commit()
    return db_membership


def get_memberships_by_user_id(db: Session, user_id: int):
    return db.query(models.Membership).filter(models.Membership.user_id == user_id).all()