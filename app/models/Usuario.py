from sqlalchemy import Column,Integer,String
from app.database import Base
from sqlalchemy.orm import relationship
class Usuario(Base):
    __tablename__ = "usuarios"
    id=Column(Integer,primary_key=True,index=True)
    nombre=Column(String)
    password=Column(String)
    tareas= relationship("Tareas",back_populates="usuario")