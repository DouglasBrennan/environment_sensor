import time
import string
import pynmea2
import serial

while True:
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline()
    print(newdata[0:6])

    if newdata[0:6] == "$GNRMC":
        newmsg = pynmea2.parse(newdata)
    lat = newmsg.latitude
    lng = newmsg.longitude
    gps = "Latitude=" + str(lat) + "Longitude=" + str(lng)
    print(gps)
