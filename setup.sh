#!/bin/bash

apt-get update -y
apt-get upgrade -y

apt-get install -y python3-venv git

# Enable GPIO serial port
sh -c 'echo "enable_uart=1" >> /boot/config.txt'

# Disable console serial port
systemctl stop serial-getty@ttyS0.service
systemctl disable serial-getty@ttyS0.service
