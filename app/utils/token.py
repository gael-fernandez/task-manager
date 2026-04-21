from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.database import SessionLocal
from app.models.Usuario import Usuario
import jwt
from app.utils.security import SECRET_KEY,ALGORITHM
oauth2=OAuth2PasswordBearer(tokenUrl="login")
def obtener_usuario_actual(token:str = Depends(oauth2)):
    db=SessionLocal()
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        sub=payload.get("sub")
        if sub is None:
            raise HTTPException(status_code=401,detail="Usuario no valido")
        usuario=db.query(Usuario).filter(Usuario.id==int(sub)).first()
        if usuario is None:
            raise HTTPException(status_code=401,detail="Usuario no valido")
        return usuario
    except Exception as e :
        raise HTTPException(status_code=401, detail=f"token invalido {e}")
    finally:
        db.close()
        