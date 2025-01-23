#!/usr/bin/python3

"""This file sill setup the FastAPI app
with a routhing logic"""

from app.routes import weather
from fastapi import FastAPI


"""Initializing the FastAPI app"""
app = FastAPI(
        title="Weather API",
        description="A weather application with current, forcast, historical, alerts, and astronomy data.",
        version="1.0.0",
        )

"""Including weather related routes"""
app.include_routes(weather.router)

"""adding a path operation decorator"""
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Weather API!"}
