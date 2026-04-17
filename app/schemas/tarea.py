from pydantic import BaseModel,ConfigDict
class CreateTarea(BaseModel):
    descripcion:str
    estado:str
    usuario_id:int

class ResponseTarea(BaseModel):
    id:int
    descripcion:str
    estado:str
    usuario_id:int
    model_config= ConfigDict(from_attributes=True)
   
class UpdateTarea(BaseModel):
    estado:str