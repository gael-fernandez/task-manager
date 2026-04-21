from fastapi import APIRouter,Depends
from app.models.Usuario import Usuario
from app.database import SessionLocal
from app.schemas.usuario import UsuarioCreate,UsuarioLogin,UsuarioResponse,UsuarioUpdate
from app.utils.security import hash_password,verificar_password,crear_token
from app.utils.token import obtener_usuario_actual
from fastapi import HTTPException   
router=APIRouter()
@router.post("/usuarios",response_model=UsuarioResponse)
def crear_usuario(usuario:UsuarioCreate):
    db = SessionLocal()
    try:
        nuevo=Usuario(nombre=usuario.nombre,password=hash_password(usuario.password))
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return nuevo
    finally:
        db.close()

@router.post("/login")
def login(nuevo_usuario:UsuarioLogin):
    db=SessionLocal()
    try:
        usuario=db.query(Usuario).filter(Usuario.nombre ==nuevo_usuario.nombre).first()
        if not usuario:
            raise HTTPException(status_code=401,detail="credenciales incorrectas")
        if not verificar_password(nuevo_usuario.password,usuario.password):
                raise HTTPException(status_code=401,detail="credenciales incorrectas")
        datos={"sub":str(usuario.id)}
        token=crear_token(datos)
        return{
    "access_token": token,
    "token_type": "bearer"}

    finally:    
        db.close()
        

@router.get("/me",response_model=UsuarioResponse)  
def mi_perfil(usuario_actual:Usuario=Depends(obtener_usuario_actual)):
        return usuario_actual

@router.put("/me",response_model=UsuarioResponse) 
def actualizar_usuario(datos_nuevos:UsuarioUpdate,usuario_actual:Usuario=Depends(obtener_usuario_actual)):
    db=SessionLocal()
    try:
        usuario=db.query(Usuario).filter(Usuario.id==usuario_actual.id).first()
        if usuario is None:
            raise HTTPException(status_code=404,detail="Usuario no encontrado")
        usuario.nombre=datos_nuevos.nombre
        usuario.password=hash_password(datos_nuevos.password)
        db.commit()
        db.refresh(usuario)
        return usuario


    finally:
        db.close()                     
@router.delete("/me") 
def delete(usuario_actual:Usuario=Depends(obtener_usuario_actual)):
    db=SessionLocal()
    try:
        usuario=db.query(Usuario).filter(Usuario.id==usuario_actual.id).first()
        if usuario is None:
            raise HTTPException(status_code=404,detail="Usuario no encontrado")
        db.delete(usuario)
        db.commit()
        return {"mensaje":"Usuario eliminado con exito"}

    finally:
        db.close()           
