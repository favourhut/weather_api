# Weather API

## Overview

The **Weather API** provides endpoints to access weather data such as current weather, weather forecasts, astronomy data (sunrise and sunset times), and historical weather data. The API fetches data from an external weather service and returns it in a structured format.

This project uses **FastAPI** for creating the web application and **httpx** for making asynchronous HTTP requests to the external Weather API. The project also includes multiple endpoints for retrieving various types of weather-related data.

## Features

- **Current Weather:** Get the current weather data for a specified location.
- **Weather Forecast:** Get the weather forecast for a specified location for a specified number of days.
- **Astronomy Data:** Get astronomy-related data, such as sunrise and sunset times for a given location on a specified date.
- **Historical Data:** Get historical weather data for a specific location and date.
- **Weather Alerts:** Get weather alerts for a given location.

## Requirements

To run this project, you need to have the following dependencies installed:

- `fastapi` - The web framework used for building the API.
- `uvicorn` - ASGI server to run the FastAPI application.
- `httpx` - To make asynchronous HTTP requests to the external Weather API.
- `pydantic` - Data validation and settings management.
- `python-dotenv` - To load environment variables from a `.env` file.

### Install Dependencies

Create a virtual environment and install the dependencies using the following commands:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows, use venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt
```

## Environment Configuration

This project uses environment variables to store sensitive data such as the API key. To configure the application, create a `.env` file at the root of the project and add the following variables:

```env
WEATHER_API_BASE_URL=https://api.weatherapi.com/v1
WEATHER_API_KEY=your_api_key_here
```

Make sure to replace `your_api_key_here` with your actual Weather API key.

### Loading Environment Variables

The project uses the `load_env()` function to load environment variables. Make sure you call this function at the start of your application.

## Running the Application

You can run the application with the following command:

```bash
uvicorn app.main:app --reload
```

This will start the FastAPI server locally at `http://127.0.0.1:8000`.

## Available Endpoints

### 1. **Current Weather**

**Endpoint:** `/weather/current`

**Method:** `GET`

**Query Parameters:**
- `location` (string): The location for which to fetch the current weather (e.g., `London`).

**Example Call:**

```bash
curl "http://127.0.0.1:8000/weather/current?location=London"
```

### 2. **Weather Forecast**

**Endpoint:** `/weather/forecast`

**Method:** `GET`

**Query Parameters:**
- `location` (string): The location for which to fetch the weather forecast (e.g., `New York`).
- `days` (int): The number of days for the forecast (e.g., `3`).

**Example Call:**

```bash
curl -X GET "http://127.0.0.1:8000/weather/forecast?location=New%20York&days=3"
```

### 3. **Astronomy Data**

**Endpoint:** `/weather/astronomy`

**Method:** `GET`

**Query Parameters:**
- `location` (string): The location for which to fetch astronomy data (e.g., `Sydney`).
- `date` (string): The date for which to fetch the data (format: `YYYY-MM-DD`, e.g., `2025-01-01`).

**Example Call:**

```bash
curl "http://127.0.0.1:8000/weather/astronomy?location=Sydney&date=2025-01-01"
```

### 4. **Historical Data**

**Endpoint:** `/weather/history`

**Method:** `GET`

**Query Parameters:**
- `location` (string): The location for which to fetch historical data (e.g., `Paris`).
- `date` (string): The date for which to fetch the historical data (format: `YYYY-MM-DD`, e.g., `2025-01-01`).

**Example Call:**

```bash
curl "http://127.0.0.1:8000/weather/history?location=Paris&date=2025-01-01"
```

## Bash Scripts for Common API Calls

To make interacting with the API easier, we have provided a set of bash scripts for the most common API calls.

### 1. **Get Current Weather**

Run the following script to get the current weather for London:

```bash
./get_current_weather.sh
```

### 2. **Get Weather Forecast**

Run the following script to get the 3-day weather forecast for New York:

```bash
./get_weather_forecast.sh
```

### 3. **Get Astronomy Data**

Run the following script to get the astronomy data (sunrise/sunset) for Sydney on 2025-01-01:

```bash
./get_astronomy_data.sh
```

### Script Files

- `get_current_weather.sh`:
  
  ```bash
  #!/bin/bash
  curl "http://127.0.0.1:8000/weather/current?location=London"
  ```

- `get_weather_forecast.sh`:
  
  ```bash
  #!/bin/bash
  curl -X GET "http://127.0.0.1:8000/weather/forecast?location=New%20York&days=3"
  ```

- `get_astronomy_data.sh`:
  
  ```bash
  #!/bin/bash
  curl "http://127.0.0.1:8000/weather/astronomy?location=Sydney&date=2025-01-01"
  ```

Make sure to give the scripts executable permissions:

```bash
chmod +x get_current_weather.sh
chmod +x get_weather_forecast.sh
chmod +x get_astronomy_data.sh
```

## Conclusion

This project provides a simple and easy-to-use weather API for retrieving real-time weather data, forecasts, astronomy data, and historical weather information. The included bash scripts allow for quick access to commonly used endpoints.