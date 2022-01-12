from flask import Flask, render_template, request
import subprocess, sys
import os
import time
import RPi.GPIO as GPIO
ledPin = 13
GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
GPIO.setup(ledPin, GPIO.OUT) # set the ledPin to OUTPUT mode
GPIO.output(ledPin, GPIO.LOW) # make ledPin output LOW level 
GPIO.setwarnings(False)

def switch_light():
    if (GPIO.input(ledPin) == 0):
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        GPIO.output(ledPin, GPIO.LOW)

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
    if (request.method == 'POST'):
        print("posted")
        switch_light()
    return render_template('index.html')

@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    #if 'Cache-Control' not in response.headers:
    response.headers['Cache-Control'] = 'no-store'
    return response

if __name__ == "__main__":
  app.run(debug=True)
