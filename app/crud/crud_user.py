from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.schemmas import schemas
from ..db.session import get_db
from ..models.user import User


def get_user_by_email(db: Session, email: str):
   
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session):
     return db.query(User).all()


def create_user(user: schemas.UserCreate, db: Session):
     existing_user = db.query(User).filter(User.email == user.email).first()
     
     new_user = User(
         email=user.email,
         full_name=user.full_name,
         password=hash_password(user.password),
         is_owner=user.is_owner
     )

     db.add(new_user)
     db.commit()
     db.refresh(new_user)

     return new_user
    

def get_user (user_id: int, db: Session):
    user = db.query(User). filter(User.id ==user_id).first()
    return user


def update_user(

    user_id: int,
    user_data: schemas.UserUpdate,
    db: Session
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    if user_data.full_name is not None:
        user.full_name = user_data.full_name
    if user_data.email is not None:
        user.email = user_data.email
    if user_data.password is not None:
        user.password = user_data.password
    if user_data.is_owner is not None:
        user.is_owner = user_data.is_owner

    db.commit()
    db.refresh(user)
    return user

def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    db.delete(user)
    db.commit()
    return {"mensaje": "Usuario eliminado"}

