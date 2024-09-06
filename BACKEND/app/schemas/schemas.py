# Aqui van a ir todas las clases de pydantic que se necesiten para el backend
from pydantic import BaseModel
from datetime import datetime, date


class Schema_user_post(BaseModel):  # Cambiado el nombre de la clase a PascalCase
    username: str
    email: str
    password: str
    date_creation: date = datetime.now().date()  
    name: str
    last_name: str
    
    # id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # username = Column(String, index=True, nullable= False)  # Añadido índice para 'name' si es buscado frecuentemente
    # email = Column(String, unique=True, index=True, nullable=False )  # 'unique' para evitar duplicados y 'index' para búsquedas rápidas
    # password = Column(String, nullable=False)  # Considera usar un hash en lugar de almacenar contraseñas en texto claro
    # date_creation = Column(Date, nullable=False)  # 'nullable' para que no se requiera una contraseña
    # name = Column(String, nullable=True)  # 'nullable' para que no se requiera una contraseña
    # last_name = Column(Date, nullable=True)