from fastapi import FastAPI
from app.routers import usuarios,tareas
import app.models
app=FastAPI()
app.include_router(usuarios.router)
app.include_router(tareas.router)
