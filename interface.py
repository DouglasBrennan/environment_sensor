from dataclasses import dataclass
from typing import Protocol


@dataclass
class Weather:
    temperature: float
    pressure: float
    humidity: float

@dataclass
class Light:
    lux: float
    proximity: float

@dataclass
class Location:
    longitude: float
    latitude: float
    altitude: float

@dataclass
class Reading:
    timestamp: int
    weather: Weather
    light: Light
    location: Location


class Sensor(Protocol):
    def get_reading(self) -> Reading:
        ...
