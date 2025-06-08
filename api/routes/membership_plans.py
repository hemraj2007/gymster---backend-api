# api/routes/membership_plans.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.schemas.membership_plans import MembershipPlanCreate, MembershipPlanUpdate, MembershipPlanOut
from api.crud import membership_plans as crud
from api.database.connection import get_db

router = APIRouter()

@router.post("/add", response_model=MembershipPlanOut)
def create_plan(plan: MembershipPlanCreate, db: Session = Depends(get_db)):
    return crud.create_plan(db, plan)

@router.get("/all", response_model=list[MembershipPlanOut])
def get_all(db: Session = Depends(get_db)):
    return crud.get_all_plans(db)

@router.get("/{plan_id}", response_model=MembershipPlanOut)
def get_by_id(plan_id: int, db: Session = Depends(get_db)):
    plan = crud.get_plan_by_id(db, plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@router.put("/update/{plan_id}", response_model=MembershipPlanOut)
def update(plan_id: int, plan_data: MembershipPlanUpdate, db: Session = Depends(get_db)):
    updated = crud.update_plan(db, plan_id, plan_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Plan not found")
    return updated

@router.delete("/delete/{plan_id}")
def delete(plan_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_plan(db, plan_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Plan not found")
    return {"msg": "Deleted successfully"}
