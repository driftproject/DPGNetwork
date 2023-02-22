from pydantic import BaseModel


class RatingSend(BaseModel):
    points: int
    time: int