from fastapi import APIRouter

from services.openweathermap import get_weather_data

router = APIRouter()

@router.get("/{city}", response_model=dict)
async def get_city(city):
    weather_data = get_weather_data(city)
    return weather_data
