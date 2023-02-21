from sqlmodel import select, create_engine, SQLModel, Session
from virtual_environment import env
from security.password import PasswordHash
from security.jwt import create_token
from player.validation.player import RegUser, AuthUser
from player.db.models.player import Player

engine = create_engine(env["POSTGRES_PATH"])
SQLModel.metadata.create_all(engine)
session = Session(engine)

def register_user(userdata: RegUser):
    player = Player(
        username=userdata.username,
        email=userdata.email,
        hashed_password=PasswordHash.get_password_hash(userdata.password),
        secret_key=PasswordHash.get_password_hash(userdata.secret_key)
    )
    session.add(player)
    session.commit()
    return_data = {
        "id": player.id,
        "username": player.username,
        "token": create_token(
            {
                "id": player.id,
                "username": player.username
            }
        )
    }