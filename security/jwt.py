from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException


def create_token(data: dict):
    to_encode = data.copy()
    exp = datetime.now() + timedelta(days=7)
    to_encode.update({'exp': exp})
    encoded_jwt = jwt.encode(to_encode, "secretkey", algorithm="HS256")
    return encoded_jwt


def verify_token(token: str):
    try:
        decoded_token = jwt.decode(token, "secretkey", algorithms=["HS256"])
        login = decoded_token.get('login')
        if login:
            return login
        raise HTTPException(status_code=400, detail='Invalid token')
    except JWTError:
        raise HTTPException(status_code=400, detail='Invalid token')


def decode_token(token: str):
    try:
        return jwt.decode(token, "secretkey", algorithms=["HS256"])
    except JWTError:
        raise HTTPException(status_code=400, detail='Invalid token')