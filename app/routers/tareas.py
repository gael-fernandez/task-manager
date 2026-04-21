from fastapi import APIRouter,HTTPException,Depends
from app.models.Tarea import Tareas
from app.models.Usuario import Usuario
from app.database import SessionLocal
from app.schemas.tarea import CreateTarea,ResponseTarea,UpdateTarea
from app.utils.token import obtener_usuario_actual
router=APIRouter()
@router.post("/tareas",response_model=ResponseTarea)
def crear_tarea(datos_entrantes:CreateTarea,usuario_actual:Usuario=Depends(obtener_usuario_actual)):
    db=SessionLocal()
    try:
        
        tarea_nueva=Tareas(descripcion=datos_entrantes.descripcion,estado=datos_entrantes.estado,usuario_id=usuario_actual.id)
        db.add(tarea_nueva)
        db.commit()
        db.refresh(tarea_nueva)
        return tarea_nueva
    finally:
        db.close()

@router.get("/tareas",response_model=list[ResponseTarea])
def lista_tareas(usuario_actual:Usuario=Depends(obtener_usuario_actual)):
    db=SessionLocal()
    try:
        tareas=db.query(Tareas).filter(Tareas.usuario_id == usuario_actual.id).all()
        return tareas
    finally:
        db.close()

@router.put("/tareas/{id}",response_model=ResponseTarea) 
def actualizar(id:int,datos:UpdateTarea,usuario_actual:Usuario=Depends(obtener_usuario_actual)):
    db=SessionLocal()
    try:
        tarea=db.query(Tareas).filter(Tareas.id == id).first()
        
        if tarea is None:
            raise HTTPException(status_code=404,detail="Tarea no encontrada")
        if tarea.usuario_id != usuario_actual.id:
           raise HTTPException(status_code=403, detail="No tienes permiso para modificar esta tarea")
        tarea.estado=datos.estado
        db.commit()
        db.refresh(tarea)
        return tarea
    finally:
        db.close()           
@router.delete("/tareas/{id}")
def eliminar(id:int,usuario_actual:Usuario=Depends(obtener_usuario_actual)):
    db=SessionLocal()
    try:
        tarea=db.query(Tareas).filter(Tareas.id==id).first()
        if tarea is None:
            raise HTTPException(status_code=404,detail="Tarea no encontrada")
        if tarea.usuario_id != usuario_actual.id:
            raise HTTPException(status_code=403,detail="No tienes permiso para eliminar esta tarea")
        db.delete(tarea)
        db.commit()
        return {"mensaje":"Tarea eliminada correctamente"}

    finally:
        db.close()    