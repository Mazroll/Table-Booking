from jose import JWTError, jwt
from decouple import config
from datetime import datetime, timedelta


def create_jwt_token(data: dict, expires_delta: timedelta = None):
    
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)  # Default expiration time

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config('SECRET_KEY'), algorithm=config('ALGORITHM'))
    return encoded_jwt