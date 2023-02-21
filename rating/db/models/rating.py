from sqlmodel import SQLModel, Field
from player.db.models import player
from datetime import datetime


class Rating(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='player.id')
    points: int
    time: int
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)