import time

from interface import Sensor, Reading, Weather, Light, Location


class DevSensor(Sensor):
    def get_reading(self) -> Reading:
        weather = Weather(
            temperature=25.0,
            pressure=630.5,
            humidity=105.3,
        )
        light = Light(
            lux=105.0,
            proximity=20.0
        )
        location = Location(
            latitude=47.37689,
            longitude=8.54802,
            altitude=450.8
        )
        return Reading(
            timestamp=time.time_ns(),
            weather=weather,
            light=light,
            location=location
        )
