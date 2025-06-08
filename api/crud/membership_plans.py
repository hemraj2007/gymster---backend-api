# api/crud/membership_plan.py
from sqlalchemy.orm import Session
from api.database.models.membership_plans import MembershipPlan
from api.database.schemas.membership_plans import MembershipPlanCreate, MembershipPlanUpdate

def create_plan(db: Session, plan: MembershipPlanCreate):
    new_plan = MembershipPlan(**plan.dict())
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return new_plan

def get_all_plans(db: Session):
    return db.query(MembershipPlan).all()

def get_plan_by_id(db: Session, plan_id: int):
    return db.query(MembershipPlan).filter(MembershipPlan.id == plan_id).first()

def update_plan(db: Session, plan_id: int, plan_data: MembershipPlanUpdate):
    plan = get_plan_by_id(db, plan_id)
    if plan:
        for key, value in plan_data.dict().items():
            setattr(plan, key, value)
        db.commit()
        db.refresh(plan)
    return plan

def delete_plan(db: Session, plan_id: int):
    plan = get_plan_by_id(db, plan_id)
    if plan:
        db.delete(plan)
        db.commit()
    return plan
