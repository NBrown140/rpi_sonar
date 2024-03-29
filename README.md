# rpi_sonar

| <img src="doc/PXL_20220918_143724242-min.jpg" alt="drawing" width="200"/> | <img src="doc/PXL_20220917_160154237-min.jpg" alt="drawing" width="200"/> | <img src="doc/PXL_20220917_160205434-min.jpg" alt="drawing" width="200"/>  |


# Setup

## Raspberry Pi 3

1. Start by installing an OS in headless mode on a raspberry pi. Connect via ssh.
2. git clone this repository.
3. 
  ```
  sudo apt-get update -y
  sudo apt-get upgrade -y
  sudo ./setup.sh
  ```
4. Edit `/boot/cmdline.txt`. Remove the line: `console=serial0,115200` and save and reboot for changes to take effect.
5. Setup python virtual environment:
   - `python3 -m venv ~/venv/gps`
   - `source ~/venv/gps/bin/activate`
   - `pip install -U pip setuptools`
   - `pip install -r requirements.txt`

Resources:
- Serial port conflict with bluetooth (very useful): https://spellfoundry.com/2016/05/29/configuring-gpio-serial-port-raspbian-jessie-including-pi-3-4/
- Tutorial to setup on Raspberry Pi: https://sparklers-the-makers.github.io/blog/robotics/use-neo-6m-module-with-raspberry-pi/
- Tutorial for GPSD: https://maker.pro/raspberry-pi/tutorial/how-to-use-a-gps-receiver-with-raspberry-pi-4
- pynmea with serial example: https://openbase.com/python/pynmea2

# Use

## Development

To start the script in development:
```console
/home/pi/venv/gps/bin/python main.py
```


To start in background mode:
```console
python main.py >/dev/null &
```

Kill with
```
kill PID
```
where PID is the process id.

## Deploy with Systemd

```console
mkdir - ~/.config/systemd/user
cp sonar.service ~/.config/systemd/user

sudo loginctl enable-linger $USER  # Make user's systemd  instance independent from user's session. Will start even if no login. May not be necessary.

systemctl --user daemon-reload
systemctl --user start sonar.service  # To start the process. 
systemctl --user stop sonar.service  # To stop the process
systemctl --user status sonar.service  # To view service status
systemctl --user enable sonar.service  # To start on boot
systemctl --user disable sonar.service  # To stop starting on boot
```

# GPS

NMEA 0183 sentences for GPS will start with different letters dependening on their constellation of origin: https://github.com/SlashDevin/NeoGPS#nmea-0183

Table with meaning of NMEA sentences for GPS: http://aprs.gids.nl/nmea/#rmc


# Ping Sonar

- https://github.com/bluerobotics/ping-python

# Resources:
Systemd:
- https://github.com/torfsen/python-systemd-tutorial
- https://unix.stackexchange.com/a/479977
- https://unix.stackexchange.com/a/251225

GPS:
- https://maker.pro/raspberry-pi/tutorial/how-to-use-a-gps-receiver-with-raspberry-pi-4
- https://maker.pro/raspberry-pi/tutorial/how-to-read-gps-data-with-python-on-a-raspberry-pi

Sonar:


 
