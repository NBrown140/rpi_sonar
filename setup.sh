#!/bin/bash

apt-get update -y
apt-get upgrade -y

# # Install gpsd
# apt-get install gpsd gpsd-clients

# # Disable default gpsd service
# systemctl disable gpsd.socket

# # Start a new gpsd instance that redirects the data of the correct serial port to a socket
# gpsd /dev/serial0 -F /var/run/gpsd.sock
