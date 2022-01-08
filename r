#!/bin/bash
export FLASK_APP=/home/pi/py_web/app.py
export FLASK_ENV=development
sudo flask run -h 192.168.0.194 -p 80
