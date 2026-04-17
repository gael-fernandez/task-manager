from pydantic import BaseModel,ConfigDict
class UsuarioCreate(BaseModel):
    nombre:str
    password:str
class UsuarioLogin(BaseModel):
    nombre:str
    password:str

class UsuarioResponse(BaseModel):
    id:int
    nombre:str
    model_config= ConfigDict(from_attributes=True)
    
class UsuarioUpdate(BaseModel):
    nombre : str
    password : str


