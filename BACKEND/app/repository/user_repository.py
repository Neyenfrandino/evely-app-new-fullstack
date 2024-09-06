# Aqui van a ir todas las funciones que se necesiten para el backend
from app.db.models import User

def create_user(schema, db):
    user_dict = dict(schema)

    user_true = db.query(User).filter(User.email == user_dict["email"]).first()

    if user_true is None:
        user = User(**user_dict)
        db.add(user)
        db.commit()
        return {"message": "User created successfully"}
    else:
        return {"message": "User already exists"}

def read_users(user_id, db):
    user_true = db.query(User).filter(User.id == user_id).first()

    if user_true is None:
        return {"message": "User not found"}
    
    return user_true

def update_user(user_id, schema, db):
    user_dict = dict(schema)
    user_true = db.query(User).filter(User.id == user_id).first()
    print(user_dict)
    if user_true is None:
        return {"message": "User not found"}
    else:
        for key, value in user_dict.items():
            if value != 'string' and value != '' : 
                setattr(user_true, key, value)

        db.add(user_true)
        db.commit()
        return {"message": "User updated successfully"}
    
def delete_user(user_id, db):
    user_true = db.query(User).filter(User.id == user_id).first()
    if user_true is None:
        return {"message": "User not found"}
    else:
        db.delete(user_true)
        db.commit()
        return {"message": "User deleted successfully"}