# rpi_sonar

# Setup

## Raspeberry Pie 3

Start by installing an OS in headless mode on a raspberry pie. Connect via ssh.



```
sudo raspi-config
```
-> Interfcaing options -> Serial -> Disable serial shell login, enable serial ports

Run the setup script form this repository:
```
sudo ./setup.sh
```


# Resources:
GPS:
- https://maker.pro/raspberry-pi/tutorial/how-to-use-a-gps-receiver-with-raspberry-pi-4
- https://maker.pro/raspberry-pi/tutorial/how-to-read-gps-data-with-python-on-a-raspberry-pi

Sonar:
- 
