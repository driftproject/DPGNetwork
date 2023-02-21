from pydantic import BaseModel, EmailStr


class RegUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    secret_key: str

class AuthUser(BaseModel):
     username: str
     password: str