from sqlmodel import select, create_engine, SQLModel, Session
from virtual_environment import env
from security.password import PasswordHash
from security.jwt import create_token, decode_token
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
        "token": {
            "access_token": create_token(
                {
                    "id": player.id,
                    "username": player.username
                }),
                "token_type": "bearer"
        }
    }
    return return_data


def login_user(userdata):
    player = session.execute(select(Player).where(Player.username == userdata.username))
    player = player.scalar_one_or_none()
    if player:
        if PasswordHash.verify_password(userdata.password, player.hashed_password):
            access_token = create_token({
                "id": player.id,
                "username": player.username
            }
            )
            return {"access_token": access_token, "token_type": "bearer"}
        elif PasswordHash.verify_password(userdata.password, player.secret_key):
            access_token = create_token({
                "id": player.id,
                "username": player.username
            }
                        )
            return {"access_token": access_token, "token_type": "bearer"}
        else:
            return Response("Incorrect password", 401)
    else:
       return Response("Incorrect password", 401)


def get_current_user_with_jwt(token):
    profile_data = decode_token(token)
    if profile_data:
        profile = session.exec(select(Player).where(Player.id == profile_data["id"])).first()
        return {
            "email": profile.email,
            "profile_pic_path": profile.profile_pic_path,
            "username": profile.username,
            "id": profile.id,
        }
    else:
        return "This token incorrect"
