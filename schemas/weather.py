#!/usr/bin/python3

"""This file validate and parse the 
response data from the WeatherAPI"""
from pydantic import BaseModel
from typing import List, Optional

# Model for Current Weather Response
class WeatherResponse(BaseModel):
    location: dict
    current: dict

    class Config:
        """Allow for extra fields in the response 
        from the API that we may not define"""
        
        extra = "allow"

class ForecastResponse(BaseModel):
    """Model for Forecast Response"""
    location: dict
    forecast: dict

    class Config:
        extra = "allow"

class HistoricalResponse(BaseModel):
    """Model for Historical Weather Response"""
    location: dict
    historical: dict

    class Config:
        extra = "allow"

class AlertsResponse(BaseModel):
    """Model for Alerts Response"""
    alerts: Optional[List[dict]] = None

    class Config:
        extra = "allow"

class AstronomyResponse(BaseModel):
    """Model for Astronomy (Sunrise/Sunset) Response"""
    astronomy: dict

    class Config:
        extra = "allow"
