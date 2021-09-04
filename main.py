import csv
import io
from datetime import datetime, timezone
from pathlib import Path

import pynmea2
import serial
from brping import Ping1D
from pynmea2.types.talker import GGA, GLL, GSA

# GGA: Fix data
# GLL: Geographic position
# GSA: DOP and active satellites

now = datetime.now(timezone.utc)
CSV_FILE = Path(Path.home(), f"sonar_{now.strftime('%y-%m-%dT%H%M%SZ')}.csv")
GPS_PORT, GPS_BAUD = "/dev/serial0", 9600
SONAR_PORT, SONAR_BAUD = "/dev/ttyUSB0", 9600

# Initialize Ping Sonar
myPing = Ping1D()
myPing.connect_serial(SONAR_PORT, SONAR_BAUD)
if myPing.initialize() is False:
    print("Failed to initialize Ping!")
    exit(1)

# Initialize GPS
ser = serial.Serial(GPS_PORT, GPS_BAUD, timeout=1.0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

# Main loop
first_iter = True
while 1:
    try:
        # Read GPS serial
        line = sio.readline()
        msg = pynmea2.parse(line)
        print(type(msg))
        if isinstance(msg, GGA):
            print(repr(msg))
            print(msg.timestamp, msg.latitude, msg.longitude, msg.gps_qual, msg.horizontal_dil, msg.altitude, msg.num_sats)
        else:
            continue
        # Read Sonar
        data = myPing.get_distance()
        if data:
            ping_distance, ping_confidence = data["distance"], data["confidence"]
            print("Distance: %s\tConfidence: %s%%" % (ping_distance, ping_confidence))
            # Write to csv
            with open(CSV_FILE, 'a', newline='') as csvfile:
                fieldnames = ["timestamp", "latitude", "longitude", "hdop", "altitude", "num_sats", "ping_distance", "ping_confidence"]
                writer = csv.DictWriter(csvfile, fieldnames, delimiter=',')
                if first_iter:
                    writer.writeheader()
                writer.writerow({
                    "timestamp": msg.timestamp, 
                    "latitude": msg.latitude,
                    "longitude": msg.longitude,
                    "hdop": msg.horizontal_dil,
                    "altitude": msg.altitude,
                    "num_sats": msg.num_sats,
                    "ping_distance": ping_distance,
                    "ping_confidence": ping_confidence
                })
                first_iter = False
        else:
            print("Failed to get distance data")
        

    except serial.SerialException as e:
        print('Device error: {}'.format(e))
        break
    except pynmea2.ParseError as e:
        print('Parse error: {}'.format(e))
        continue


