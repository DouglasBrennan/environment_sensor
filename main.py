import datetime

import raspi_sensor
import storage


def main():
    sensor = raspi_sensor.RaspiSensor()
    reading = sensor.get_reading()
    database = storage.Database()
    database.write_reading(reading)
    print(f'Wrote reading at {datetime.datetime.fromtimestamp(reading.timestamp)} to database.')


if __name__ == '__main__':
    main()
