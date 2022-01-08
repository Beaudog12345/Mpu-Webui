from flask import Flask, render_template
import subprocess, sys
import os
import time
sys.path.insert(1, '/home/pi/Mpu-Webui/mpu')
import MPU6050
import time
mpu = MPU6050.MPU6050()
mpu.dmp_initialize()
y = 0
p = 0
r = 0
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', r=r, p=p, y=y)
@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response

if __name__ == "__main__":
  app.run(debug=True)
