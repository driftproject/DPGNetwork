from sqlmodel import SQLModel, Field


class Player(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(max_length=20, min_length=5)
    email: str
    hashed_password: str
    profile_pic_path: str
    secret_key: str