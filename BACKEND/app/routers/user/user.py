# Aqui van a ir todas las rutas del usuario, todos los endpoints que se necesiten para el usuario
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends
from app.routers.api_router.api_router import api_router
from app.schemas.schemas import Schema_user
from app.db.database import get_db
from sqlalchemy.orm import Session

from app.db.models import User


# router = api_router(prefix="user", tags=["user"])
router = APIRouter(prefix=f"/user", tags=["user"])


# @router.post("/")
# def read_users(schema_user: Schema_user):
#     # Convertir el esquema en un diccionario
#     user = dict(schema_user)
#     print(user)  # Esto se verá en la consola donde estés corriendo FastAPI
    
#     return {
#         "message": "Hello World",
#         "user": user  # O puedes retornar los datos del usuario si es necesario
#     }

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    # Aqui se puede hacer cualquier consulta a la base de datos 
    # Por ejemplo, si queremos obtener todos los usuarios de la base de datos
    users = db.query(User).all()
    return users