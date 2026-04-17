from sqlalchemy import Column,String,Integer
from sqlalchemy import ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship
class Tareas(Base):
    __tablename__="tareas"
    id=Column(Integer,primary_key=True,index=True)
    descripcion=Column(String)
    estado=Column(String)
    usuario_id=Column(Integer,ForeignKey("usuarios.id"))
    usuario=relationship("Usuario",back_populates="tareas")
    