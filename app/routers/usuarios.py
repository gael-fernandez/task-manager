from fastapi import APIRouter
from models import Usuario
from database import SessionLocal
from schemas.usuario import UsuarioCreate,UsuarioLogin,UsuarioResponse
from utils.security import hash_password,verificar_password
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
        