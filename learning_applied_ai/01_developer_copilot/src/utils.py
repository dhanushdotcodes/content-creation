import requests
from datetime import datetime
from zoneinfo import ZoneInfo

from schema import (
    JokeResponse,
    WeatherResponse,
    GeoCodingResponse,
    CurrencyRateResponse,
)

def get_weather(city: str):
    """
    Returns current weather for a city.

    Returns:
        dict
    """

    # Step 1: Get latitude and longitude
    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_response = requests.get(
        geocode_url,
        params={"name": city, "count": 1},
        timeout=10,
    )

    geo_response.raise_for_status()

    geo = GeoCodingResponse.model_validate(geo_response.json())

    if not geo.results:
        return {
            "error": f"Could not find city '{city}'."
        }

    location = geo.results[0]

    # Step 2: Fetch weather

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_response = requests.get(
        weather_url,
        params={
            "latitude": location.latitude,
            "longitude": location.longitude,
            "current": "temperature_2m,wind_speed_10m",
        },
        timeout=10,
    )

    weather_response.raise_for_status()

    weather = WeatherResponse.model_validate(weather_response.json())

    return {
        "city": location.name,
        "country": location.country,
        "temperature": weather.current.temperature_2m,
        "temperature_unit": weather.current_units.temperature_2m,
        "wind_speed": weather.current.wind_speed_10m,
        "wind_speed_unit": weather.current_units.wind_speed_10m,
        "time": weather.current.time,
        "timezone": weather.timezone,
    }


def get_random_joke():
    """
    Returns a random joke.
    """

    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    joke = JokeResponse.model_validate(response.json())

    return {
        "setup": joke.setup,
        "punchline": joke.punchline,
        "type": joke.type,
        "id": joke.id,
    }


def get_current_time(timezone: str):
    """
    Example:
        Asia/Kolkata
        Europe/London
        America/New_York
    """

    try:
        now = datetime.now(ZoneInfo(timezone))
    except Exception:
        return {
            "error": f"Invalid timezone '{timezone}'."
        }

    return {
        "timezone": timezone,
        "current_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "day": now.strftime("%A"),
        "iso": now.isoformat(),
    }


def currency_convertor(
    amount: float,
    from_currency: str,
    to_currency: str,
):
    """
    Converts currency using Frankfurter API.
    """

    base = from_currency.upper()
    quote = to_currency.upper()
    url = f"https://api.frankfurter.dev/v2/rate/{base}/{quote}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    rate_data = CurrencyRateResponse.model_validate(response.json())
    rate = rate_data.rate
    converted = amount * rate

    return {
        "amount": amount,
        "from": rate_data.base,
        "to": rate_data.quote,
        "exchange_rate": rate,
        "converted_amount": round(converted, 2),
        "date": rate_data.date,
    }