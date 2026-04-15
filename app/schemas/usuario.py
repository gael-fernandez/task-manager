from pydantic import BaseModel
class UsuarioCreate(BaseModel):
    nombre:str
    password:str