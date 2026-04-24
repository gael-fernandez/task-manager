from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import usuarios, tareas
import app.models
from app.database import engine, Base
from app.models import Usuario, Tarea

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="API de gestión de tareas con autenticación JWT",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "https://frontend-task-manager-proyecto-de-port-gael-fernandezs-projects.vercel.app",
    "https://frontend-task-manager-proyecto-de-portafolio-p9u3fouod.vercel.app",
    "https://frontend-task-manager-proyecto-de-p.vercel.app",
    "https://frontend-task-manager-proye-git-22f6c2-gael-fernandezs-projects.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios.router)
app.include_router(tareas.router)