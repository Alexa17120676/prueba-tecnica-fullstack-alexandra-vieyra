# Problema A: Agrupación de datos
showtimes = [
    {"movie": "Inside Out 3", "cine": "Perisur", "format": "IMAX", "tickets_sold": 120},
    {"movie": "Inside Out 3", "cine": "Perisur", "format": "2D", "tickets_sold": 85},
    {"movie": "Inside Out 3", "cine": "Santa Fe", "format": "2D", "tickets_sold": 90},
    {"movie": "Deadpool 4", "cine": "Perisur", "format": "3D", "tickets_sold": 200},
    {"movie": "Deadpool 4", "cine": "Santa Fe", "format": "IMAX", "tickets_sold": 180},
    {"movie": "Moana 3", "cine": "Perisur", "format": "2D", "tickets_sold": 60},
]


def summarize_by_movie(showtimes):
    movies = {}
    for showtime in showtimes:
        movie = showtime["movie"]
        tickets = showtime["tickets_sold"]

        if movie not in movies:
            movies[movie] = {
                "total_shows": 0,
                "total_tickets": 0
            }
        movies[movie]["total_shows"] += 1
        movies[movie]["total_tickets"] += tickets

    result = []

    for movie, data in movies.items():
        avg = round(data["total_tickets"] / data["total_shows"], 2)

        result.append({
            "movie": movie,
            "total_shows": data["total_shows"],
            "total_tickets": data["total_tickets"],
            "avg_tickets": avg
        })

    result.sort(
        key=lambda item: item["total_tickets"],
        reverse=True
    )
    return result

# Problema B: Validación de horarios

def time_to_minutes(time):
    hours, minutes = time.split(":")

    return int(hours) * 60 + int(minutes)

def minutes_to_time(total_minutes):
    total_minutes = total_minutes % (24 * 60)

    hours = total_minutes // 60
    minutes = total_minutes % 60

    return f"{hours:02d}:{minutes:02d}"

def validate_showtime(start_time: str, duration_min: int, opening: str, closing: str) -> dict:
    start = time_to_minutes(start_time)
    open_time = time_to_minutes(opening)
    close_time = time_to_minutes(closing)

    end = start + duration_min

    if start < open_time:
        return {
            "valid": False,
            "reason": f"Starts before opening ({opening})"
        }
    if end >= close_time:
        end_time = minutes_to_time(end)
        return {
            "valid": False,
            "reason": f"Ends after closing ({end_time} >= {closing})"
        }
    return {"valid": True}

if __name__ == "__main__":
    print(summarize_by_movie(showtimes))

    print(validate_showtime("14:30", 120, "10:00", "23:00"))
    print(validate_showtime("09:00", 90, "10:00", "23:00"))
    print(validate_showtime("21:30", 150, "10:00", "23:00"))