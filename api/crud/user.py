from sqlalchemy.orm import Session
from api.database.models.user import User
from api.database.schemas.user import UserCreate, UserUpdate, UserProfileUpdate
from datetime import datetime
from api.security import hash_password

# Create new user
def create_user(db: Session, user: UserCreate):
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hash_password(user.password),
        mobile=user.mobile,
        age=user.age,
        gender=user.gender,
        role=user.role,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get all users
def get_all_users(db: Session):
    return db.query(User).all()

# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Get user by mobile number
def get_user_by_mobile(db: Session, mobile: str):  # Fixed argument name
    return db.query(User).filter(User.mobile == mobile).first()  # Fixed field name

# Get user by ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Update user details
def update_user_profile(db: Session, user_id: int, updated_data: UserProfileUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    # Updated data ke fields ko user object me set karo
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Update user password (only new password)
def update_user_password(db: Session, user_id: int, new_password: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    user.password = hash_password(new_password)
    user.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(user)
    return user

# Delete user by ID
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    db.delete(user)
    db.commit()
    return user

# Update user profile
def update_user_profile(db: Session, user_id: int, updated_data: UserProfileUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    # Update the user profile fields if provided
    if updated_data.first_name:
        user.first_name = updated_data.first_name

    if updated_data.last_name:
        user.last_name = updated_data.last_name

    if updated_data.email:
        user.email = updated_data.email
    
    if updated_data.mobile:
        user.mobile = updated_data.mobile

    # Update the timestamp when the profile is updated
    user.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    db.delete(user)
    db.commit()
    return user
