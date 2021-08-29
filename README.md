# rpi_sonar

# Setup

## Raspberry Pie 3

Start by installing an OS in headless mode on a raspberry pie. Connect via ssh.

Serial port conflict with bluetooth: https://spellfoundry.com/2016/05/29/configuring-gpio-serial-port-raspbian-jessie-including-pi-3-4/

Tutorial for GPSD: https://maker.pro/raspberry-pi/tutorial/how-to-use-a-gps-receiver-with-raspberry-pi-4

<!-- ```
sudo raspi-config
```
-> Interfacing options -> Serial -> Disable serial shell login, enable serial ports

Run the setup script from this repository:
```
sudo ./setup.sh
``` -->



# GPS

NMEA 0183 sentences for GPS will start with different letters dependening on their constellation of origin: https://github.com/SlashDevin/NeoGPS#nmea-0183

Table with meaning of NMEA sentences for GPS: http://aprs.gids.nl/nmea/#rmc

Tui=torial to setup on Raspberry Pie: https://sparklers-the-makers.github.io/blog/robotics/use-neo-6m-module-with-raspberry-pi/

# Ping Sonar


# Resources:
GPS:
- https://maker.pro/raspberry-pi/tutorial/how-to-use-a-gps-receiver-with-raspberry-pi-4
- https://maker.pro/raspberry-pi/tutorial/how-to-read-gps-data-with-python-on-a-raspberry-pi

Sonar:
- 
