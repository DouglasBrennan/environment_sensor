# environment_sensor

This repository contains scripts to be run on a [Raspberry Pi](https://www.raspberrypi.com) connected to an [Enviro+](https://shop.pimoroni.com/products/enviro?variant=31155658457171) for environment sensing.

## Setup
In order to set up the raspberry, install the [Raspberry Pi OS](https://www.raspberrypi.com/software/) onto it by following their [instructions](https://youtu.be/ntaXWS8Lk34).

after that, run the following commands:
`sudo apt-get update`
`sudo apt-get upgrade`
`sudo apt-get install python3-dev python3-pip`
`curl -sSL https://get.pimoroni.com/enviroplus | bash`
`pip3 install -r requirements.txt`

## Running the sensor
In order to run the sensor, you can manually start it with the command `python3 main.py`.

Output can be adapted to be sent to the ledger via [iota-communicator](https://github.com/DouglasBrennan/hackIota/blob/master/app.py).

Alternatively, output can also be sent to a [Redis-TimeSeries](https://redis.io/docs/stack/timeseries/). (Needs to be initialized by following their [setup guide](https://redis.io/docs/getting-started/)).
