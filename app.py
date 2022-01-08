from flask import Flask, render_template
import subprocess, sys
import os
import time
sys.path.insert(1, '/home/pi/py_web/mpu')
import MPU6050
import time
mpu = MPU6050.MPU6050()
mpu.dmp_initialize()
y = 0
p = 0
r = 30
y = y + 180
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', y=y, p=p, r=r)

if __name__ == "__main__":
  app.run(debug=True)
