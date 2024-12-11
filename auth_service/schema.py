from pydantic import BaseModel, EmailStr
from enum import Enum

class Role(str, Enum):
    Admin = "Admin"
    Attendant = "Attendant"
    Staff = "Staff"

class UserBase(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    phone_number: str
    role: Role

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
