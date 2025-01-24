#!/usr/bin/python3

""" """

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Location(BaseModel):
    name: str
    region: str
    country: str
    localtime: str

class Condition(BaseModel):
    text: str

class Current(BaseModel):
    temp_c: float
    temp_f: float
    is_day: int
    condition: Condition
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float

class FilteredWeatherResponse(BaseModel):
    location: Location
    current: Current

@app.get("/weather/current", response_model=FilteredWeatherResponse)
def get_current_weather(location: str):
    # Simulated API response (replace with actual API call)
    api_response = {
        "location": {
            "name": "London",
            "region": "City of London, Greater London",
            "country": "United Kingdom",
            "lat": 51.5171,
            "lon": -0.1062,
            "tz_id": "Europe/London",
            "localtime_epoch": 1737733412,
            "localtime": "2025-01-24 15:43",
        },
        "current": {
            "last_updated_epoch": 1737732600,
            "last_updated": "2025-01-24 15:30",
            "temp_c": 10.1,
            "temp_f": 50.2,
            "is_day": 1,
            "condition": {"text": "Sunny", "icon": "//icon_url", "code": 1000},
            "wind_mph": 13.4,
            "wind_kph": 21.6,
            "humidity": 50,
            "cloud": 0,
            "feelslike_c": 7.4,
            "feelslike_f": 45.2,
        },
    }

    # Extract only required fields
    filtered_response = {
        "location": {
            "name": api_response["location"]["name"],
            "region": api_response["location"]["region"],
            "country": api_response["location"]["country"],
            "localtime": api_response["location"]["localtime"],
        },
        "current": {
            "temp_c": api_response["current"]["temp_c"],
            "temp_f": api_response["current"]["temp_f"],
            "is_day": api_response["current"]["is_day"],
            "condition": {
                "text": api_response["current"]["condition"]["text"],
            },
            "humidity": api_response["current"]["humidity"],
            "cloud": api_response["current"]["cloud"],
            "feelslike_c": api_response["current"]["feelslike_c"],
            "feelslike_f": api_response["current"]["feelslike_f"],
        },
    }

    return filtered_response
