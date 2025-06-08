from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.database.schemas.user import UserResponse, PasswordUpdate, UserProfileUpdate
from api.token import get_current_user
from api.database.connection import get_db
from api.database import models  # Importing models
from api.crud import user as user_crud  # Importing user CRUD functions

router = APIRouter()

# Profile fetch
@router.get("/profile", response_model=UserResponse)
def get_profile(current_user: UserResponse = Depends(get_current_user)):
    return current_user

# Password Update (without current password)
@router.put("/update_password")
def update_password(
    data: PasswordUpdate,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verify new password == confirm password
    if data.new_password != data.confirm_password:
        raise HTTPException(status_code=400, detail="New password and confirm password do not match.")

    # Update password
    updated_user = user_crud.update_user_password(db, current_user.id, data.new_password)
    if not updated_user:
        raise HTTPException(status_code=500, detail="Something went wrong while updating password.")

    return {"message": "Password updated successfully."}

# Update Profile
@router.put("/update_profile/{user_id}", response_model=UserResponse)
def update_profile(
    user_id: int,
    updated_data: UserProfileUpdate,
    db: Session = Depends(get_db),
):
    user = user_crud.update_user_profile(db, user_id, updated_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = user_crud.get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="No users found.")
    return users

# Get user by ID
@router.get("/user/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user

# Delete user by ID
@router.delete("/user/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"message": f"User with ID {user_id} has been deleted successfully."}