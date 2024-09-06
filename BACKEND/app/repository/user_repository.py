# Aqui van a ir todas las funciones que se necesiten para el backend
from app.db.models import User

def create_user( schema, db):
    user_dict = dict(schema)

    user_true = db.query(User).filter(User.email == user_dict["email"]).first()

    if user_true is None:
        user = User(**user_dict)
        db.add(user)
        db.commit()
        return {"message": "User created successfully"}
    else:
        return {"message": "User already exists"}
