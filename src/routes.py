from fastapi import APIRouter, Query, HTTPException
from typing import List
from src.data.services import get_city
from src.data.models import City
from src.data.schemas import CityBase
from db import get_database

router = APIRouter()

def calculate_distance(lat1, lon1, lat2, lon2):
    # Calculate the Euclidean distance between two points
    return ((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2) ** 0.5

def calculate_score(distance):
    # Calculate the score based on the distance
    if distance <= 1.0:
        return 1.0
    elif distance <= 5.0:
        return 0.9
    elif distance <= 10.0:
        return 0.8
    else:
        return 0.5

@router.get("/suggestions")
async def suggest_cities(q: str = Query(..., min_length=1), latitude: float = None, longitude: float = None):
    try:
        db = get_database()  # Get the database instance
        cities = get_city(db)  # Retrieve cities from the database

        filtered_cities = [city for city in cities if q.lower() in city.name.lower()]  # Filter the cities based on the search query

        # Check if latitude and longitude are provided
        if latitude is not None and longitude is not None:
            # Calculate the Euclidean distance and score for each city
            for city in filtered_cities:
                city.distance = calculate_distance(latitude, longitude, city.lat, city.long)
                city.score = calculate_score(city.distance)

            # Sort the cities based on the score
            sorted_cities = sorted(filtered_cities, key=lambda city: city.score, reverse=True)

            # Normalize the scores based on the maximum score
            max_score = sorted_cities[0].score if sorted_cities else 1.0
            for city in sorted_cities:
                city.score /= max_score

            # Generate the suggestion response
            suggestions = [
                {
                    "name": city.name,
                    "latitude": str(city.lat),
                    "longitude": str(city.long),
                    "score": city.score
                }
                for city in sorted_cities
            ]
        else:
            suggestions = []  # No latitude and longitude provided, return an empty list of suggestions

        suggestions = suggestions[:10]  # Limit to 10 records

        return {"suggestions": suggestions}
    except Exception as e:
        # Handle any exception that occurred during the request
        raise HTTPException(status_code=500, detail=str(e))
