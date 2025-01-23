#!/usr/bin/python3

"""This class handle requests to the WeatherAPI"""
  
import httpx
from app.config import Config
from typing import Any
from app.schemas.weather import WeatherResponse, ForecastResponse, HistoricalResponse, AlertsResponse, AstronomyResponse


class WeatherService:
    """class to handle requests to the WeatherAPI
    """
    
    def __init__(self):
        self.base_url = Config.WEATHER_API_BASE_URL
        self.api_key = Config.WEATHER_API_KEY

    def _get_url(self, endpoint: str, params: dict) -> str:
        """Helper method to construct the URL"""
        
        params["key"] = self.api_key
        url = f"{self.base_url}/{endpoint}"
        return url, params

    async def get_current_weather(self, location: str) -> WeatherResponse:
        """Get current weather data"""
        
        url, params = self._get_url("current.json", {"q": location})
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
        response.raise_for_status()  # Will raise an error if the request fails
        return WeatherResponse(**response.json())

    async def get_forecast(self, location: str, days: int) -> ForecastResponse:
        """Get weather forecast"""
        
        url, params = self._get_url("forecast.json", {"q": location, "days": days})
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
        response.raise_for_status()
        return ForecastResponse(**response.json())

    async def get_historical_weather(self, location: str, date: str) -> HistoricalResponse:
        """Get historical weather data"""
        
        url, params = self._get_url("history.json", {"q": location, "dt": date})
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
        response.raise_for_status()
        return HistoricalResponse(**response.json())

    """Get weather alerts"""
    async def get_alerts(self, location: str) -> AlertsResponse:
        url, params = self._get_url("alerts.json", {"q": location})
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
        response.raise_for_status()
        return AlertsResponse(**response.json())

    """Get astronomy data (sunrise/sunset)"""
    async def get_astronomy_data(self, location: str, date: str) -> AstronomyResponse:
        url, params = self._get_url("astronomy.json", {"q": location, "dt": date})
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
        response.raise_for_status()
        return AstronomyResponse(**response.json())
