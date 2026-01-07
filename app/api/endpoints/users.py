from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemmas.schemas import UserCreate, UserOut, UserUpdate
from app.crud import crud_user

router = APIRouter()



@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends()):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    return crud_user.create_user(db=db, user=user)


@router.get("/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends()):
    return crud_user.get_users(db)


@router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends()):
    db_user = crud_user.get_user(user_id,db )
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user


@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user_in: UserUpdate, db: Session = Depends()):
    db_user = crud_user.get_user(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return crud_user.update_user(user_id, db_user)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends()):
    db_user = crud_user.get_user(user_id,db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    crud_user.delete_user(db=db, user_id=user_id)
    return None # 204 No Content no devuelve cuerpo