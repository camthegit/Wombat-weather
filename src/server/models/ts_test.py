from datetime import datetime

from beanie import Document, TimeSeriesConfig, Granularity
from pydantic import Field
from typing import Optional


# TODO: add beanie, pydantic, pymongo to requirements


class WeatherTS(Document):
    ts: datetime = Field(default_factory=datetime.now)
    source: dict
    temp: Optional[float]
    pressure: Optional[float]
    humidity: Optional[float]
    direction: Optional[float]
    speed: Optional[float]
    gust: Optional[float]
    rain: Optional[float]
    cpuTemp: Optional[float]
    skyTemp: Optional[float]
    ambientTemp: Optional[float]

    class Settings:
        timeseries = TimeSeriesConfig(
            time_field="ts",
            meta_field="source",
            granularity=Granularity.hours,
            # expire_after_seconds=2  # Optional
        )
        name = "weatherObs"

    class Config:
        schema_extra = {
            "example": {
                "source": {"sensorId": "DHT22", "type": "temperature", "location": "Wombats End"},
                "timestamp": datetime.now(),
                "temp": 11
            }
        }


class WeatherAGG(Document):
    year: int
    month: int
    day: int
    hour: int
    source: str
    avgTemp: Optional[float]
    avgPressure: Optional[float]
    avgHumidity: Optional[float]
    avgDirection: Optional[float]
    avgSpeed: Optional[float]
    avgGust: Optional[float]
    avgCpuTemp: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "year": 2022,
                "month": 7,
                "day": 11,
                "hour": 15,
                "source": "DHT22",
                "avgTemp": 13.4
            }
        }
