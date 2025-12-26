from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from database import SessionLocal
import schemas
from fastapi import FastAPI
from database import engine
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

@app.post("/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    new_user = models.User(
        email=user.email,
        password=user.password,
        is_owner=user.is_owner
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "mensaje": "Usuario creado correctamente",
        "user_id": new_user.id
    }
