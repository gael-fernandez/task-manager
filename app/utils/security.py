from passlib.context import CryptContext
from datetime import datetime, timedelta,timezone
import jwt
SECRET_KEY = "s3cr3t_3h3jnjn21jn"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password:str):
    return pwd_context.hash(password)
def verificar_password(password_entrante:str,password_hasheada:str):
    return pwd_context.verify(password_entrante,password_hasheada)

def crear_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"]=expire
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

