from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.crud import membership as crud
from api.database.schemas import membership as schemas

router = APIRouter()

@router.post("/add", response_model=schemas.MembershipResponse)
def add_membership(membership: schemas.MembershipCreate, db: Session = Depends(get_db)):
    return crud.create_membership(db, membership)

@router.get("/all", response_model=list[schemas.MembershipResponse])
def get_all_memberships(db: Session = Depends(get_db)):
    return crud.get_all_memberships(db)

@router.get("/get/{membership_id}", response_model=schemas.MembershipResponse)
def get_membership_by_id(membership_id: int, db: Session = Depends(get_db)):
    result = crud.get_membership_by_id(db, membership_id)
    if not result:
        raise HTTPException(status_code=404, detail="Membership not found")
    return result

@router.put("/update_status/{membership_id}")
def update_status(membership_id: int, status: schemas.PaymentStatusEnum, db: Session = Depends(get_db)):
    updated_membership = crud.update_membership_status(db, membership_id, status)
    if not updated_membership:
        raise HTTPException(status_code=404, detail="Membership not found")
    return {"message": "Status updated successfully"}

@router.delete("/delete/{membership_id}")
def delete_membership(membership_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_membership(db, membership_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Membership not found")
    return {"message": "Membership deleted successfully"}


@router.get("/user/{user_id}", response_model=list[schemas.MembershipResponse])
def get_memberships_by_user_id(user_id: int, db: Session = Depends(get_db)):
    memberships = crud.get_memberships_by_user_id(db, user_id)
    if not memberships:
        raise HTTPException(
            status_code=404, 
            detail=f"No memberships found for user with id {user_id}"
        )
    return memberships