from pydantic import BaseModel, EmailStr
from typing import Optional

# Create User Schema (used in registration)
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    mobile: str
    age:int
    gender:str
    role: str


# Login Schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Update User Schema
class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    mobile: Optional[str]
    age: Optional[int]       # ✅ Fix: Optional banaya
    gender: Optional[str]

    class Config:
        from_attributes = True

# Response Schema (used in API responses)
class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    mobile: str
    age:int
    gender:str
    role: str

    class Config:
        from_attributes = True

# Password Update Schema (without current password)
class PasswordUpdate(BaseModel):
    new_password: str
    confirm_password: str


class UserProfileUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    mobile: str
    age: Optional[int]       # ✅ Fix: Optional banaya
    gender: Optional[str]

    class Config:
        from_attributes = True