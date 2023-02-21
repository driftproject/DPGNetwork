from sqlmodel import select, create_engine, SQLModel, Session
from virtual_environment import env
from security.password import PasswordHash
from security.jwt import create_token
from player.validation.player import RegUser, AuthUser
from player.db.models.player import Player
from random import randint
from fastapi.responses import FileResponse
from fastapi import Response

engine = create_engine(env["POSTGRES_PATH"])
SQLModel.metadata.create_all(engine)
session = Session(engine)


def register_user(userdata: RegUser):
    player = Player(
        username=userdata.username,
        email=userdata.email,
        hashed_password=PasswordHash.get_password_hash(userdata.password),
        secret_key=PasswordHash.get_password_hash(userdata.secret_key),
        profile_pic_path=f"logo{randint(1,6)}.png"
    )
    session.add(player)
    session.commit()
    return_data = {
        "id": player.id,
        "username": player.username,
        "profile_pic": player.profile_pic_path,
        "token": create_token(
            {
                "id": player.id,
                "username": player.username
            }
        )
    }
    return return_data


def login_user(userdata: AuthUser):
    player = session.execute(select(Player).where(Player.username == userdata.username))
    player = player.scalar_one_or_none()
    if player:
        if PasswordHash.verify_password(userdata.password, player.hashed_password):
            return {
                "id": player.id,
                "username": player.username,
                "profile_pic": player.profile_pic_path,
                "token": create_token(
                    {
                        "id": player.id,
                        "username": player.username
                    }
                )
            }
        elif PasswordHash.verify_password(userdata.password, player.secret_key):
            return {
                "id": player.id,
                "username": player.username,
                "profile_pic": player.profile_pic_path,
                "token": create_token(
                {
                    "id": player.id,
                    "username": player.username
                }
                )
        }
        else:
            return Response("Incorrect password", 401)
    else:
        return Response("Incorrect password", 401)