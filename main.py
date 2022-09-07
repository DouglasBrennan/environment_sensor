from datetime import datetime
import time
import os

import raspi_sensor
import storage


def main():
    sensor = raspi_sensor.RaspiSensor()
    database = storage.Database()
    # priming sensor
    for i in range(10):
        sensor.get_reading()
    while True:
        reading = sensor.get_reading()
        database.write_reading(reading)
        print(f'Wrote reading to database at {datetime.now()}.')
        storage.push_to_tangle(reading)
        print(f'Pushed reading to tangle with index {os.getenv("uuid")}.')
        time.sleep(1)


if __name__ == '__main__':
    main()
