import time
import sys
sys.path.insert(1, '/home/pi/Mpu-Webui/mpu')
import MPU6050
gyro = [0]*3
y = 0
mpu = MPU6050.MPU6050()
mpu.dmp_initialize()

while True:
    gyro = mpu.get_rotation()
    y = str(gyro[0])
    #print(y)
    f = open("static/y.txt", "w")
    f.write(y)
    f.close()
    time.sleep(0.1)
