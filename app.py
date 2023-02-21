from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from virtual_environment import env
from player.player_routes import _player_routing



app = FastAPI()
app.include_router(
    _player_routing
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

