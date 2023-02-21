from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from virtual_environment import env

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
