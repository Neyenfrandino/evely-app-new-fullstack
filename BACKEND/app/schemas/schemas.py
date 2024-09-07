# Aqui van a ir todas las clases de pydantic que se necesiten para el backend
from pydantic import BaseModel
from datetime import datetime, date
from typing import Union


class Schema_user(BaseModel):  # Cambiado el nombre de la clase a PascalCase
    username: str
    email: str
    password: str
    date_creation: date = datetime.now().date()  
    name: str
    last_name: str

    class Config:
        orm_mode = True  # Permite crear instancias desde objetos ORM (como los de SQLAlchemy)
        from_attributes = True # Permite usar from_orm para crear instancias desde atributos de objetos ORM

class Schema_user_login(BaseModel):
    email: str
    password: str
    class Config:
        orm_mode = True  # Permite crear instancias desde objetos ORM (como los de SQLAlchemy)
        from_attributes = True # Permite usar from_orm para crear instancias desde atributos de objetos ORM


class token(BaseModel):
    access_token: str
    token_type: str

class token_data(BaseModel):
    username: Union[str, None] = None
    email: Union[str, None] = None