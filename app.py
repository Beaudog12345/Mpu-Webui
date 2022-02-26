from flask import Flask, render_template, request
import subprocess, sys
import os
import time
import RPi.GPIO as GPIO
motorPin = 13
GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
GPIO.setup(motorPin, GPIO.OUT) # set the motorPin to OUTPUT mode
GPIO.output(motorPin, GPIO.LOW) # make motorPin output LOW level 
GPIO.setwarnings(False)

def switch_motor():
    if (GPIO.input(motorPin) == 0):
        GPIO.output(motorPin, GPIO.HIGH)
    else:
        GPIO.output(motorPin, GPIO.LOW)

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
    if (request.method == 'POST'):
        print("posted")
        switch_motor()
    return render_template('index.html')

@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    #if 'Cache-Control' not in response.headers:
    response.headers['Cache-Control'] = 'no-store'
    return response

if __name__ == "__main__":
  app.run(debug=True)
