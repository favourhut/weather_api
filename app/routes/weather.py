#!/usr/bin/python3

"""This file defines endpoints for accessing the WeatherAPI"""

# app/routes/weather.py

from app.services.weather_service import WeatherService
from app.schemas.weather import WeatherResponse, ForecastResponse, HistoricalResponse, AlertsResponse, AstronomyResponse
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)

def get_weather_service():
    return WeatherService()

@router.get("/current", response_model=WeatherResponse)
async def get_current_weather(location: str, weather_service: WeatherService = Depends(get_weather_service)):
    try:
        return await weather_service.get_current_weather(location)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/forecast", response_model=ForecastResponse)
async def get_weather_forecast(location: str, days: int, weather_service: WeatherService = Depends(get_weather_service)):
    try:
        return await weather_service.get_forecast(location, days)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history", response_model=HistoricalResponse)
async def get_historical_weather(location: str, date: str, weather_service: WeatherService = Depends(get_weather_service)):
    try:
        return await weather_service.get_historical_weather(location, date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/alerts", response_model=AlertsResponse)
async def get_weather_alerts(location: str, weather_service: WeatherService = Depends(get_weather_service)):
    try:
        return await weather_service.get_alerts(location)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/astronomy", response_model=AstronomyResponse)
async def get_astronomy_data(location: str, date: str, weather_service: WeatherService = Depends(get_weather_service)):
    try:
        return await weather_service.get_astronomy_data(location, date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
