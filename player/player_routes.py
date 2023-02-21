from fastapi import APIRouter
from player.validation.player import RegUser, AuthUser
from player.db

_player_routing = APIRouter(
    prefix="/player"
)

@_player_routing.post("/registration")