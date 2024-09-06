# Aqui van a ir todas las rutas del usuario, todos los endpoints que se necesiten para el usuario
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.schemas.schemas import Schema_user_post
from app.db.database import get_db
# from app.db.models import User
from app.repository.user_repository import create_user

router = APIRouter(prefix=f"/user", tags=["user"])


@router.post("/create_user")
def read_users(schema_user: Schema_user_post, db: Session = Depends(get_db)):
    # Convertir el esquema en un diccionario
    response = create_user( schema_user, db)
    return response


@router.get("/")
def read_users(db: Session = Depends(get_db)):
    # Aqui se puede hacer cualquier consulta a la base de datos 
    # Por ejemplo, si queremos obtener todos los usuarios de la base de datos
    # users = db.query(User).all()
    # return users
    pass