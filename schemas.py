from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    is_owner: bool



class UserCreate(BaseModel):
    email: str
    full_name: str  
    password: str
    is_owner: bool

class UserUpdate(BaseModel):
    full_name: str | None = None 
    email: EmailStr | None = None 
    password: str | None = None
    is_owner: bool | None = None

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True


