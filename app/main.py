from fastapi import FastAPI
from app.routers import usuarios
import app.models
app=FastAPI()
app.include_router(usuarios.router)