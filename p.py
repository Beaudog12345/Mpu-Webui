import time
import sys
sys.path.insert(1, '/home/pi/Mpu-Webui/mpu')
import MPU6050
gyro = [0]*3
p = 0
mpu = MPU6050.MPU6050()
mpu.dmp_initialize()

while True:
    gyro = mpu.get_rotation()
    p = str(gyro[1])
    #print(p)
    f = open("static/p.txt", "w")
    f.write(p)
    f.close()
    time.sleep(0.1)
