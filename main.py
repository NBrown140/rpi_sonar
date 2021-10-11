import csv
import io
from datetime import datetime, timezone
import time

from pathlib import Path

import pynmea2
import serial
from brping import Ping1D
from pynmea2.types.talker import GGA, RMC

# GGA: Fix data
# GLL: Geographic position
# GSA: DOP and active satellites

GPS_PORT, GPS_BAUD = "/dev/serial0", 9600
SONAR_PORT, SONAR_BAUD = "/dev/ttyUSB0", 9600
MAX_TRY_INIT = 5
DEBUG = False 

# Start initialization loop
initialized = False
num_try_init = 0
while not initialized and num_try_init < MAX_TRY_INIT:
    if num_try_init < MAX_TRY_INIT:
        try:
            # Initialize Ping Sonar
            myPing = Ping1D()
            myPing.connect_serial(SONAR_PORT, SONAR_BAUD)
            if myPing.initialize() is False:
                raise Exception("Failed to initialize Ping!")
            # Initialize GPS
            ser = serial.Serial(GPS_PORT, GPS_BAUD, timeout=1.0)
            sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
            initialized = True
        except Exception as e:
            print(str(e))
            print("Initialization failed. Waiting 5 sec and starting over.")
            time.wait(5)
            num_try_init += 1
    else:
        print(f"Max number of initialization tries ({MAX_TRY_INIT}) exceeded")
        exit(1)

# Main loop
first_iter = True
first_datetime = None
while 1:
    try:
        # Read GPS serial
        line = sio.readline()
        msg = pynmea2.parse(line)
        if DEBUG:
            print(type(msg))
        # Do different actions based on GPS message type
        if isinstance(msg, RMC):
            print(repr(msg))
            date = msg.datestamp
            time = msg.timestamp
            if first_datetime is None:
                first_datetime = f"{date.year}-{date.month:02}-{date.day:02}T{time.hour:02}{time.minute:02}{time.second:02}Z"
                print(f"Using first_datetime: {first_datetime}")
            continue
        elif isinstance(msg, GGA):
            print(repr(msg))
        else:
            continue
        # Don't enter rest of loop if no GPS date
        if first_datetime is None:
            print("first_datetime is None, skipping sonar reading for now")
            continue
        # Read Sonar
        ping_data = myPing.get_distance()
        if ping_data:
            print("Distance: %s\tConfidence: %s%%" % (ping_data["distance"], ping_data["confidence"]))
            # Write to csv
            csv_file = Path(Path.home(), f"sonar_{first_datetime}.csv")
            with open(csv_file, 'a', newline='') as csvfile:
                fieldnames = ["datestamp", "timestamp", "latitude", "longitude", "hdop", "altitude", "num_sats", "ping_distance", "ping_confidence"]
                writer = csv.DictWriter(csvfile, fieldnames, delimiter=',')
                if first_iter:
                    writer.writeheader()
                row = {
                    "datestamp": date,
                    "timestamp": msg.timestamp, 
                    "latitude": msg.latitude,
                    "longitude": msg.longitude,
                    "hdop": msg.horizontal_dil,
                    "altitude": msg.altitude,
                    "num_sats": msg.num_sats,
                    "ping_distance": ping_data["distance"],
                    "ping_confidence": ping_data["confidence"]
                }
                writer.writerow(row)
                print(f"Wrote row: {row}")
                first_iter = False
        else:
            print("Failed to get distance data")
        

    except serial.SerialException as e:
        print('Device error: {}'.format(e))
        break
    except pynmea2.ParseError as e:
        print('Parse error: {}'.format(e))
        continue


