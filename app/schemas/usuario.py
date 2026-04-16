from pydantic import BaseModel
class UsuarioCreate(BaseModel):
    nombre:str
    password:str
class UsuarioLogin(BaseModel):
    nombre:str
    password:str

class UsuarioResponse(BaseModel):
    id:int
    nombre:str
    
class UsuarioUpdate(BaseModel):
    nombre : str
    password : str


