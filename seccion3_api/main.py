from datetime import date
from typing import Optional, List

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel


app = FastAPI(title="Cinema API")


class Showtime(BaseModel):
    id_showtime: int
    id_movie: int
    movie: str
    show_time: str


class Room(BaseModel):
    id_room: int
    name: str
    showtimes: List[Showtime]


class CinemaResponse(BaseModel):
    id_cine: int
    name: str
    brand: str
    city: str
    date: str
    rooms: List[Room]


class Week(BaseModel):
    id_week: int
    week_number: int
    init_date: str
    end_date: str
    movies_count: int


class WeeksResponse(BaseModel):
    data: List[Week]


cinemas = {
    15: {
        "id_cine": 15,
        "name": "Perisur",
        "brand": "VIP",
        "city": "CDMX",
        "rooms": [
            {
                "id_room": 1,
                "name": "Sala 1",
                "showtimes": [
                    {
                        "id_showtime": 101,
                        "id_movie": 1,
                        "movie": "Inside Out 3",
                        "show_time": "14:30"
                    }
                ]
            }
        ]
    }
}


weeks = [
    {
        "id_week": 1,
        "week_number": 32,
        "init_date": "2026-08-03",
        "end_date": "2026-08-09",
        "movies_count": 12
    },
    {
        "id_week": 2,
        "week_number": 33,
        "init_date": "2026-08-10",
        "end_date": "2026-08-16",
        "movies_count": 8
    },
    {
        "id_week": 3,
        "week_number": 34,
        "init_date": "2026-08-17",
        "end_date": "2026-08-23",
        "movies_count": 10
    }
]


@app.get(
    "/api/v1/cines/{id_cine}",
    response_model=CinemaResponse
)
def get_cinema(
    id_cine: int,
    date_param: Optional[date] = Query(default=None, alias="date")
):
    cinema = cinemas.get(id_cine)

    if not cinema:
        raise HTTPException(
            status_code=404,
            detail="El cine solicitado no existe"
        )

    selected_date = date_param or date.today()

    return {
        **cinema,
        "date": selected_date.isoformat()
    }


@app.get(
    "/api/v1/weeks",
    response_model=WeeksResponse
)
def get_weeks(
    year: int,
    status: str = "assigned"
):
    filtered_weeks = [
        week for week in weeks
        if week["init_date"].startswith(str(year))
    ]

    return {
        "data": filtered_weeks
    }