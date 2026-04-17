from fastapi import APIRouter,HTTPException
from app.models.Tarea import Tareas
from app.models.Usuario import Usuario
from app.database import SessionLocal
from app.schemas.tarea import CreateTarea,ResponseTarea
router=APIRouter()
@router.post("/tareas",response_model=ResponseTarea)
def crear_tarea(datos_entrantes:CreateTarea):
    db=SessionLocal()
    try:
        usuario=db.query(Usuario).filter(Usuario.id == datos_entrantes.usuario_id).first()
        if usuario is None:
            raise HTTPException(status_code=404,detail="Usuario no encontrado")
        tarea_nueva=Tareas(descripcion=datos_entrantes.descripcion,estado=datos_entrantes.estado,usuario_id=datos_entrantes.usuario_id)
        db.add(tarea_nueva)
        db.commit()
        db.refresh(tarea_nueva)
        return tarea_nueva
    finally:
        db.close()