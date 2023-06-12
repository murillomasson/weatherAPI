from fastapi import FastAPI
from routes.weather import router as weather_router

app = FastAPI()

app.include_router(weather_router)
