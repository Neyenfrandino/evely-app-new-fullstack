# Aqui vamos a declarar las tablas que necesitemos para el backend y las relaciones que tengamos con otras tablas
# Esto aqui va a ser la base de nuestra base de datos y las tablas que necesitemos
# Debemos siempre asegurarnos de que estamos usando los mismos datos que estamos delcrando en schemas
from sqlalchemy import Column, Integer, String
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)  # Añadido índice para 'name' si es buscado frecuentemente
    email = Column(String, unique=True, index=True)  # 'unique' para evitar duplicados y 'index' para búsquedas rápidas
    password = Column(String)  # Considera usar un hash en lugar de almacenar contraseñas en texto claro
