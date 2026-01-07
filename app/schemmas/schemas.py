from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    is_owner: bool 

class UserCreate(BaseModel):
    email: str
    full_name: str  
    password: str
    is_owner: bool

class UserUpdate(BaseModel):
    full_name: Optional [str] | None = None 
    email: Optional [EmailStr] | None = None 
    password: Optional [str] | None = None
    is_owner: Optional [bool] | None = None



class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True


