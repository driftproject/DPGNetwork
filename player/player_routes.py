from fastapi import APIRouter
from player.validation.player import RegUser, AuthUser
from player.db.player import register_user, login_user
from fastapi.responses import FileResponse

_player_routing = APIRouter(
    prefix="/player"
)


@_player_routing.post("/registration")
async def _registration_user_(userdata: RegUser):
    return register_user(userdata)


@_player_routing.get("/profile/images/{image}")
async def return_profile_pic(image: str):
    return FileResponse(f"player/profile_pics/{image}")


@_player_routing.post("/login")
async def _login_user_(userdata: AuthUser):
    return login_user(userdata)