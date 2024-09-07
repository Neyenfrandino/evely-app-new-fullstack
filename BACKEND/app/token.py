from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_code = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_code.update({"exp": expire})
    encoded_jwt = jwt.encode(to_code, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
