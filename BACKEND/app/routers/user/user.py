# Aqui van a ir todas las rutas del usuario, todos los endpoints que se necesiten para el usuario
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.schemas.schemas import Schema_user_post
from app.db.database import get_db
# from app.db.models import User
from app.repository.user_repository import create_user, read_users, update_user, delete_user

router = APIRouter(prefix=f"/user", tags=["user"])

@router.post("/create_user")
def create_users(schema_user: Schema_user_post, db: Session = Depends(get_db)):
    # Convertir el esquema en un diccionario
    response = create_user( schema_user, db)
    return response

@router.get("/read_user")
def read_users_id(user_id:int, db: Session = Depends(get_db)):
    response = read_users(user_id, db)
    return response 

@router.patch("/update_user")
def update_users(user_id:int, schema_user: Schema_user_post, db: Session = Depends(get_db)):
    response = update_user(user_id, schema_user, db)
    return response

@router.delete("/delete_user")
def delete_users(user_id:int, db: Session = Depends(get_db)):
    response = delete_user(user_id, db)
    return response