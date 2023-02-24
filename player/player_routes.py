from fastapi import APIRouter, Depends
from player.validation.player import RegUser, AuthUser
from player.db.player import register_user, login_user, get_current_user_with_jwt, get_player_data_with_id, get_player_data_with_username
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from security.oauth import oauth2
_player_routing = APIRouter(
    prefix="/player",
    tags=["Player",]
)



@_player_routing.post("/registration")
async def _registration_user_(userdata: RegUser):
    return register_user(userdata)


@_player_routing.get("/profile/images/{image}")
async def return_profile_pic(image: str):
    return FileResponse(f"player/profile_pics/{image}")


@_player_routing.post("/login")
async def _token_getter_(userdata: AuthUser = Depends()):
    return login_user(userdata)


@_player_routing.get("/me")
async def get_player_profile(token: str = Depends(oauth2)):
    return get_current_user_with_jwt(token)


@_player_routing.get("/{id}")
async def get_player_with_id(id):
    return get_player_data_with_id(id)

@_player_routing.get("/{username}")
async def get_player_with_id(username):
    return get_player_data_with_username(username)