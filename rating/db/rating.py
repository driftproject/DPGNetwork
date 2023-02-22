from sqlmodel import select, create_engine, SQLModel, Session
from virtual_environment import env
from rating.validation.rating import RatingSend
from rating.db.models.rating import Rating


engine = create_engine(env["POSTGRES_PATH"])
SQLModel.metadata.create_all(engine)
session = Session(engine)


def create_result(rating: RatingSend, user_id):
    _rating = Rating(user_id=user_id, points=rating.points, time=rating.time, speed=rating.points/rating.time)
    session.add(_rating)
    session.commit()
    return {
    "user_id": _rating.user_id,
    "points": _rating.points,
    "time": _rating.time,
    "speed": _rating.speed
}


def get_rating_by_userid(user_id):
    _rating = session.exec(select(Rating).where(Rating.user_id == user_id)).all()
    return _rating

def get_all_rating_data():
    _rating = list(session.exec(select(Rating)).all())
    for i in range(len(_rating)-1):
        for j in range(len(_rating)-i-1):
            if  _rating[j].speed < _rating[j+1].speed:
                _rating[j], _rating[j+1] = _rating[j+1], _rating[j]
    return _rating
