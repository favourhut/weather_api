#!/usr/bin/python3

"""Configuration setting that handles envirimental
variables such as API keys"""

from dotenv import load_dotenv
import os


class Config:
    """This is a class configuration code"""

    WEATHER_API_BASE_URL = "http://api.weatherapi.com/v1"
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")