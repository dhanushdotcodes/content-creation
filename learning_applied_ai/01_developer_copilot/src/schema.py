from typing import Optional
from pydantic import BaseModel

class CalendarEvent(BaseModel):
    date: str
    place: str
    description: str

class JokeResponse(BaseModel):
    type: str
    setup: str
    punchline: str
    id: int

class CurrentUnits(BaseModel):
    time: str
    interval: str
    temperature_2m: str
    wind_speed_10m: str

class CurrentWeather(BaseModel):
    time: str
    interval: int
    temperature_2m: float
    wind_speed_10m: float

class WeatherResponse(BaseModel):
    latitude: float
    longitude: float
    generationtime_ms: float
    utc_offset_seconds: int
    timezone: str
    timezone_abbreviation: str
    elevation: float
    current_units: CurrentUnits
    current: CurrentWeather

class GeoCodingResult(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    elevation: Optional[float] = None
    feature_code: Optional[str] = None
    country_code: Optional[str] = None
    admin1_id: Optional[int] = None
    admin2_id: Optional[int] = None
    timezone: Optional[str] = None
    population: Optional[int] = None
    country_id: Optional[int] = None
    country: Optional[str] = None
    admin1: Optional[str] = None
    admin2: Optional[str] = None

class GeoCodingResponse(BaseModel):
    results: Optional[list[GeoCodingResult]] = None
    generationtime_ms: float


class CurrencyRateResponse(BaseModel):
    date: str
    base: str
    quote: str
    rate: float


