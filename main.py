from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from database import SessionLocal
import schemas
from fastapi import FastAPI
from database import engine, SessionLocal

import models

# Crea las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "Alq-APP funcionando 🚀"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    new_user = models.User(
        email=user.email,
        full_name=user.full_name,
        password=user.password,
        is_owner=user.is_owner
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
    
@app.get("/users", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends (get_db)):
    return db.query(models.User).all()



@app.get("/users{user_id}", response_model=schemas.UserOut)
def get_user (user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User). filter(models.User.id ==user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@app.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user(

    user_id: int,
    user_data: schemas.UserUpdate,
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
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

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(user)
    db.commit()
    return {"mensaje": "Usuario eliminado"}

