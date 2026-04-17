from fastapi import APIRouter
from app.models.Usuario import Usuario
from app.database import SessionLocal
from app.schemas.usuario import UsuarioCreate,UsuarioLogin,UsuarioResponse,UsuarioUpdate
from app.utils.security import hash_password,verificar_password
from fastapi import HTTPException   
router=APIRouter()
@router.post("/usuarios")
def crear_usuario(usuario:UsuarioCreate):
    db = SessionLocal()
    try:
        nuevo=Usuario(nombre=usuario.nombre,password=hash_password(usuario.password))
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return{"id":nuevo.id
            ,"nombre":nuevo.nombre}
    finally:
        db.close()

@router.post("/login")
def login(nuevo_usuario:UsuarioLogin):
    db=SessionLocal()
    try:
        usuario=db.query(Usuario).filter(Usuario.nombre ==nuevo_usuario.nombre).first()
        if not usuario:
            raise HTTPException(status_code=401,detail="credenciales incorrectas")
        else:
            if not verificar_password(nuevo_usuario.password,usuario.password):
                raise HTTPException(status_code=401,detail="credenciales incorrectas")
            else:
                return {"mensaje":"login exitoso"}

    finally:    
        db.close()
        
@router.get("/usuarios",response_model=list[UsuarioResponse])
def obtener_usuarios():
    db=SessionLocal()
    try:
        usuarios=db.query(Usuario).all()
        return usuarios
    finally:
        db.close()

@router.get("/usuarios/{id}",response_model=UsuarioResponse)  
def obtener_usuario(id:int):
    db=SessionLocal()
    try:
        usuario_id=db.query(Usuario).filter(Usuario.id==id).first()
        if usuario_id is None:
            raise HTTPException(status_code=404,detail="Usuario no encontrado")
        return usuario_id
    finally:
        db.close()

@router.put("/usuarios/{id}",response_model=UsuarioResponse) 
def actualizar_usuario(id:int,datos_nuevos:UsuarioUpdate):
    db=SessionLocal()
    try:
        usuario=db.query(Usuario).filter(Usuario.id==id).first()
        if usuario is None:
            raise HTTPException(status_code=404,detail="Usuario no encontrado")
        usuario.nombre=datos_nuevos.nombre
        usuario.password=hash_password(datos_nuevos.password)
        db.commit()
        db.refresh(usuario)
        return usuario


    finally:
        db.close()                     
@router.delete("/usuarios/{id}") 
def delete(id:int):
    db=SessionLocal()
    try:
        usuario=db.query(Usuario).filter(Usuario.id==id).first()
        if usuario is None:
            raise HTTPException(status_code=404,detail="Usuario no encontrado")
        db.delete(usuario)
        db.commit()
        return {"mensaje":"Usuario eliminado con exito"}

    finally:
        db.close()           