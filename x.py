import time
import sys
sys.path.insert(1, '/home/pi/py_web/mpu')
import MPU6050
gyro = [0]*3
x = 0
mpu = MPU6050.MPU6050()
mpu.dmp_initialize()

while True:
    gyro = mpu.get_rotation()
    x = str(gyro[0])
    print(x)
    f = open("static/x.txt", "w")
    f.write(x)
    f.close()
    time.sleep(0.1)
