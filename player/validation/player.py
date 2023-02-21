from pydantic import BaseModel, EmailStr


class RegUser(BaseModel):
    username: str
    email: EmailStr
    password: str


class AuthUser(BaseModel):
     username: str
     password: str