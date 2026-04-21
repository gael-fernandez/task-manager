from fastapi import FastAPI
from app.routers import usuarios,tareas
import app.models
app = FastAPI(
    title="Task Manager API",
    description="API de gestión de tareas con autenticación JWT",
    version="1.0.0"
)
app.include_router(usuarios.router)
app.include_router(tareas.router)
