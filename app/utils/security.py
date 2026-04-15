from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password:str):
    return pwd_context.hash(password)
def verificar_password(password_entrante:str,password_hasheada:str):
    return pwd_context.verify(password_entrante,password_hasheada)