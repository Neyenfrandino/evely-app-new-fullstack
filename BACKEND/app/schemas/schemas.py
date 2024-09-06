# Aqui van a ir todas las clases de pydantic que se necesiten para el backend
from pydantic import BaseModel

class Schema_user(BaseModel):
    name: str
    email: str
    password: str