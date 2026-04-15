from database import engine,Base
from models import Usuario,Tarea
Base.metadata.create_all(bind=engine)
