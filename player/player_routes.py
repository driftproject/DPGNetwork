from fastapi import APIRouter, Depends
from player.validation.player import RegUser, AuthUser
from player.db.player import register_user, login_user, get_current_user_with_jwt, login_user_with_jwt
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

_player_routing = APIRouter(
    prefix="/player"
)

oauth2 = OAuth2PasswordBearer(tokenUrl="/player/token")

@_player_routing.post("/registration")
async def _registration_user_(userdata: RegUser):
    return register_user(userdata)


@_player_routing.get("/profile/images/{image}")
async def return_profile_pic(image: str):
    return FileResponse(f"player/profile_pics/{image}")


@_player_routing.post("/login")
async def _login_user_(userdata: AuthUser):
    return login_user(userdata)

@_player_routing.post("/token")
async def _token_getter_(userdata: OAuth2PasswordRequestForm = Depends(), response_model=None):
    return login_user_with_jwt(userdata)

@_player_routing.get("/me")
async def get_player_profile(token: str = Depends(oauth2)):
    return get_current_user_with_jwt(token)
