from fastapi import FastAPI
from app.db.session import engine, Base
from app.api.api import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "Alq-APP funcionando 🚀"}


app.include_router(api_router, prefix="/api")