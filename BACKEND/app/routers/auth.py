from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.schemas import Schema_user_login, token
from app.db.database import get_db
from app.repository.auth import login_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=token, status_code=status.HTTP_200_OK)
def login_users(schema_user: Schema_user_login, db: Session = Depends(get_db)):
    auth_token = login_user(schema_user, db)
    return auth_token
