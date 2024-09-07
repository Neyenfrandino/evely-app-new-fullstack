from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models import User
from app.hashing import Hash
from app.token import create_access_token

def login_user(schema, db: Session):
    try:
        user_dict = dict(schema) 
        user_true = db.query(User).filter(User.email == user_dict["email"]).first()

        if user_true is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        else:
            if Hash.verify_password(user_dict["password"], user_true.password):
                access_token = create_access_token({"username": user_true.username, "email": user_true.email})
                return {"access_token": access_token, "token_type": "bearer"}
            else:
                raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
