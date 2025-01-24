#!/usr/bin/python3

"""This file validates and parses the response data from the WeatherAPI"""

from pydantic import BaseModel
from typing import List, Optional


# Model for Location metadata
class Location(BaseModel):
    """Model for location metadata"""
    name: str
    region: str
    country: str
    lat: float
    lon: float
    timezone: str


# Model for Current Weather Response
class CurrentWeather(BaseModel):
    """Model for the current weather"""
    temp_c: float
    temp_f: float
    humidity: int
    wind_kph: float
    wind_mph: float
    pressure_mb: float
    pressure_in: float
    feelslike_c: float
    feelslike_f: float


class WeatherResponse(BaseModel):
    """Model for Current Weather Response"""
    location: Location
    current: CurrentWeather


# Model for Forecast Weather Response
class ForecastWeatherDay(BaseModel):
    """Model for a single day's forecast"""
    date: str  # Date of the forecast
    maxtemp_c: float  # Max temperature in Celsius
    maxtemp_f: float  # Max temperature in Fahrenheit
    mintemp_c: float  # Min temperature in Celsius
    mintemp_f: float  # Min temperature in Fahrenheit
    avgtemp_c: float  # Average temperature in Celsius
    avgtemp_f: float  # Average temperature in Fahrenheit
    maxwind_kph: float  # Max wind speed in km/h
    maxwind_mph: float  # Max wind speed in mph
    totalprecip_mm: float  # Total precipitation in mm
    totalprecip_in: float  # Total precipitation in inches
    avghumidity: int  # Average humidity percentage

class ForecastResponse(BaseModel):
    """Model for Forecast Response"""
    location: Location
    forecast: dict  # Using a dict here because it's often a dictionary of dates with forecast details.


# Model for Historical Weather Response
class HourlyWeather(BaseModel):
    """Model for hourly weather data"""
    time: str  # The time of the observation, e.g., "2025-01-24 00:00"
    temp_c: float  # Temperature in Celsius
    humidity: int  # Humidity in percentage


class HistoricalWeatherDay(BaseModel):
    """Model for daily historical weather data"""
    date: str  # The date of the weather data, e.g., "2025-01-24"
    hour: List[HourlyWeather]  # List of hourly data for the day


class HistoricalResponse(BaseModel):
    """Model for Historical Weather Response"""
    location: Location
    historical: List[HistoricalWeatherDay]


# Model for Alerts Response
class AlertsResponse(BaseModel):
    """Model for Alerts Response"""
    alerts: Optional[List[dict]] = None


# Model for Astronomy (Sunrise/Sunset) Response
class AstronomyResponse(BaseModel):
    """Model for Astronomy (Sunrise/Sunset) Response"""
    astronomy: dict
