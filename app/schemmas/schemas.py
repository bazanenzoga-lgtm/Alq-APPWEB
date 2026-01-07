from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    is_owner: bool = False
    full_name: Optional[str] = None

class UserCreate(UserBase): # Heredamos de Base para no repetir email
    password: str

class UserUpdate(BaseModel):
    # En Pydantic v2, usar Optional[str] = None es suficiente
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_owner: Optional[bool] = None

class UserOut(UserBase): # Heredamos de Base para que incluya email, is_owner y full_name
    id: int

    # Forma moderna (Pydantic v2) de habilitar el modo ORM
    model_config = ConfigDict(from_attributes=True)
