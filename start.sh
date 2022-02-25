#!/bin/bash
export FLASK_APP=/home/pi/Mpu-Webui/app.py
export FLASK_ENV=development
sudo pkill -f flask
flask run -h 172.20.10.9
