#!/bin/bash

# Fetch weather forecast for New York for 3 days
curl -X GET "http://127.0.0.1:8000/weather/forecast?location=New%20York&days=1"

