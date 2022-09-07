import time

from smbus2 import SMBus
from bme280 import BME280
from enviroplus import gas
from ltr559 import LTR559

from interface import Sensor, Reading, Weather, Light, Location


class RaspiSensor(Sensor):
    def __init__(self):
        self.bus = SMBus(1)
        self.bme280 = BME280(i2c_dev=self.bus)
        self.ltr559 = LTR559()

    def get_reading(self) -> Reading:
        self.ltr559.update_sensor()
        weather = Weather(
            temperature=self.bme280.get_temperature(),
            pressure=self.bme280.get_pressure(),
            humidity=self.bme280.get_humidity(),
        )
        light = Light(
            lux=self.ltr559.get_lux(),
            proximity=self.ltr559.get_proximity(),
        )
        location = Location(
            latitude=47.37689,
            longitude=8.54802,
            altitude=450.8
        )
        timestamp = int(time.time() * 1000)
        print(f'timestamp: {timestamp}')
        return Reading(
            timestamp=timestamp,
            weather=weather,
            light=light,
            location=location
        )
