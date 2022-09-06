from smbus2 import SMBus
from bme280 import BME280
from enviroplus import gas
import ltr559

from interface import Sensor, Reading


class RaspiSensor(Sensor):
    def __init__(self):
        self.bus = SMBus(1)
        self.bme280 = BME280(i2c_dev=self.bus)

    def get_reading(self) -> Reading:
        return Reading(
            temperature=self.bme280.get_temperature(),
            pressure=self.bme280.get_pressure(),
            humidity=self.bme280.get_humidity(),
            lux=ltr559.get_lux(),
            proximity=ltr559.get_proximity(),
        )