# Mpu-Webui
The code in this repository is used to run a homemade flight controller, based around the Raspberry Pi Zero 2 W.

# Specs
The flight controller itself uses a 3d printed 2-part base. The raspberry pi is powered by a pisugar 2, and has header pins soldered onto 5v, GND, SDA and SCL. The attitude sensor connects to the top of the case and uses 4 female to female jumpers to connect to the pi. The case has a spot for a camera mount to attach the official raspberry pi camera.

# Code
RPY.py is ran in the background, and populates a text file with live gyro data from the MPU6050. Start.sh begins the flask web server, which has options to start, calibrate, and turn a GPIO pin on and off (in this case called motor, but could be used to toggle a status light). 

# Images
Our WIP Flight Controller
![alt text](https://github.com/Beaudog12345/Mpu-Webui/blob/main/images/IMG_2214.png?raw=true)
A render of the 3D model in solidworks
![alt text](https://github.com/Beaudog12345/Mpu-Webui/blob/main/images/Screenshot%202022-01-05%20115216.png?raw=true)
Our plane prototype
![alt text](https://github.com/Beaudog12345/Mpu-Webui/blob/main/images/IMG_2072.png?raw=true)
