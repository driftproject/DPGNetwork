from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from virtual_environment import env
from player.player_routes import _player_routing
from rating.rating_router import _rating_routing
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()
app.include_router(
    _player_routing
)

app.include_router(
    _rating_routing
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

