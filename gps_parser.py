import time

import serial
import pynmea2

while True:
    port = "/dev/ttyAMA0"
    with serial.Serial(port, baudrate=9600, timeout=0.5) as ser:
        dataout = pynmea2.NMEAStreamReader()
        newdata = ser.readline()

        if newdata[0:6] == "$GPRMC":
            newmsg = pynmea2.parse(newdata)
            lat = newmsg.latitude
            lon = newmsg.longitude
            print(f"Latitude: {lat}, Longitude: {lon}")
        print("Pausing one sec")
        time.sleep(1)