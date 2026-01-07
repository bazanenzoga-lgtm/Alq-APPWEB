from fastapi import FastAPI
from sqlalchemy import Engine
from app.db.session import SessionLocal
from app.models.user import User
from app.api.api import api_router

# Crea las tablas en la base de datos
User.metadata.create_all(bind=Engine)

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

app.include_router(api_router, prefix="/api")