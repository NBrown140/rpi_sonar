# rpi_sonar

# Setup

## Raspberry Pie 3

Start by installing an OS in headless mode on a raspberry pie. Connect via ssh.

```
sudo apt-get update -y
sudo apt-get upgrade -y
sudo ./setup.sh
```
Edit `/boot/cmdline.txt`. Remove the line: `console=serial0,115200` and save and reboot for changes to take effect.

Resources:
- Serial port conflict with bluetooth (very useful): https://spellfoundry.com/2016/05/29/configuring-gpio-serial-port-raspbian-jessie-including-pi-3-4/
- Tutorial to setup on Raspberry Pie: https://sparklers-the-makers.github.io/blog/robotics/use-neo-6m-module-with-raspberry-pi/
- Tutorial for GPSD: https://maker.pro/raspberry-pi/tutorial/how-to-use-a-gps-receiver-with-raspberry-pi-4
- pynmea with serial example: https://openbase.com/python/pynmea2


# GPS

NMEA 0183 sentences for GPS will start with different letters dependening on their constellation of origin: https://github.com/SlashDevin/NeoGPS#nmea-0183

Table with meaning of NMEA sentences for GPS: http://aprs.gids.nl/nmea/#rmc


# Ping Sonar


# Resources:
GPS:
- https://maker.pro/raspberry-pi/tutorial/how-to-use-a-gps-receiver-with-raspberry-pi-4
- https://maker.pro/raspberry-pi/tutorial/how-to-read-gps-data-with-python-on-a-raspberry-pi

Sonar:
- 
