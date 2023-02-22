from fastapi import APIRouter, Depends
from rating.validation.rating import RatingSend
from rating.db.rating import create_result, get_rating_by_userid, get_all_rating_data
from security.oauth import oauth2
import json
from security.jwt import decode_token

_rating_routing = APIRouter(
    prefix="/rating"
)

@_rating_routing.post("/create")
async def create_rating(rating: RatingSend, token: str = Depends(oauth2)):
    return create_result(rating, decode_token(token)["id"])


@_rating_routing.get("/by_user/{id}")
async def _get_rating_by_userid(id: int, token: str = Depends(oauth2)):
    return get_rating_by_userid(id)

@_rating_routing.get("/all")
async def _get_all_rating(token: str = Depends(oauth2)):
    return get_all_rating_data()