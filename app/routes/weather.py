#!/usr/bin/python3

"""This file defines endpoints for accessing the WeatherAPI"""


from app.services.weather_service import WeatherService
from app.schemas.weather import WeatherResponse, ForecastResponse, HistoricalResponse, AlertsResponse, AstronomyResponse
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)

"""Dependency to inject the weather service"""
def get_weather_service():
    return WeatherService()

"""Current weather endpoint"""
@router.get("/current", response_model=WeatherResponse)
async def get_current_weather(location: str, weather_service: WeatherService = Depends(get_weather_service)):
    
    """
    Get current weather for a given location.
    """
    try:
        return await weather_service.get_current_weather(location)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""Forecast endpoint"""
@router.get("/forecast", response_model=ForecastResponse)
async def get_weather_forecast(location: str, days: int, weather_service: WeatherService = Depends(get_weather_service)):
    """
    Get weather forecast for a given location and number of days.
    """
    try:
        return await weather_service.get_forecast(location, days)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""Historical data endpoint"""
@router.get("/history", response_model=HistoricalResponse)
async def get_historical_weather(location: str, date: str, weather_service: WeatherService = Depends(get_weather_service)):
    """
    Get historical weather for a given location and date (YYYY-MM-DD).
    """
    try:
        return await weather_service.get_historical_weather(location, date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""Alerts endpoint"""
@router.get("/alerts", response_model=AlertsResponse)
async def get_weather_alerts(location: str, weather_service: WeatherService = Depends(get_weather_service)):
    """
    Get weather alerts for a given location.
    """
    try:
        return await weather_service.get_alerts(location)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""Astronomy endpoint"""
@router.get("/astronomy", response_model=AstronomyResponse)
async def get_astronomy_data(location: str, date: str, weather_service: WeatherService = Depends(get_weather_service)):
    """
    Get astronomy data (e.g., sunrise/sunset) for a given location and date (YYYY-MM-DD).
    """
    try:
        return await weather_service.get_astronomy_data(location, date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))