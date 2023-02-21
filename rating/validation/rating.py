from pydantic import BaseModel


class RatingSend(BaseModel):
    user_id: int
    points: int
    time: int