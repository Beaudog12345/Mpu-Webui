import time
import sys
sys.path.insert(1, '/home/pi/Mpu-Webui/mpu')
import MPU6050
gyro = [0]*3
r = 0
mpu = MPU6050.MPU6050()
mpu.dmp_initialize()

while True:
    gyro = mpu.get_rotation()
    r = str(gyro[0])
    #print(r)
    f = open("static/r.txt", "w")
    f.write(r)
    f.close()
    time.sleep(0.1)
