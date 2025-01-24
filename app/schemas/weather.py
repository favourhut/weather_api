#!/usr/binpyython3


"""This file validate and parse the 
response data from the WeatherAPI"""
from pydantic import BaseModel
from typing import List, Optional

# Model for Current Weather Response
class WeatherResponse(BaseModel):
    location: dict
    current: dict

class ForecastResponse(BaseModel):
    """Model for Forecast Response"""
    location: dict
    forecast: dict

class HistoricalResponse(BaseModel):
    """Model for Historical Weather Response"""
    location: dict
    historical: dict

class AlertsResponse(BaseModel):
    """Model for Alerts Response"""
    alerts: Optional[List[dict]] = None

class AstronomyResponse(BaseModel):
    """Model for Astronomy (Sunrise/Sunset) Response"""
    astronomy: dict
