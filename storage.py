import os

from dotenv import load_dotenv
from redis import Redis
from interface import Reading

import requests

load_dotenv()

ENDPOINT = os.getenv('ENDPOINT')
PORT = os.getenv('PORT')
PASSWORD = os.getenv('PASSWORD')


class Database:
    def __init__(self, host: str = ENDPOINT, port: int = PORT, password: str = PASSWORD):
        self.store = Redis(host=host, port=port, password=password)

    def write_reading(self, reading: Reading) -> None:
        self.store.ts().add('lux', reading.timestamp, reading.light.lux)
        self.store.ts().add('proximity', reading.timestamp, reading.light.proximity)
        self.store.ts().add('pressure', reading.timestamp, reading.weather.pressure)
        self.store.ts().add('temperature', reading.timestamp, reading.weather.temperature)
        self.store.ts().add('humidity', reading.timestamp, reading.weather.humidity)
        self.store.ts().add('longitude', reading.timestamp, reading.location.longitude)
        self.store.ts().add('latitude', reading.timestamp, reading.location.latitude)
        self.store.ts().add('altitude', reading.timestamp, reading.location.altitude)


def push_to_tangle(reading: Reading) -> str:
    message_id = requests.get(
        f'https://iota-publisher.herokuapp.com/conditions?'
        f'lux={reading.light.lux}&'
        f'proximity={reading.light.proximity}&'
        f'pressure={reading.weather.pressure}&'
        f'temperature={reading.weather.temperature}&'
        f'humidity={reading.weather.humidity}&'
        f'longitude={reading.location.longitude}&'
        f'latitude={reading.location.latitude}&'
        f'altitude={reading.location.altitude}&'
        f'uuid={os.getenv("uuid")}'
    )
    return str(message_id)
