import time
import sys
sys.path.insert(1, '/home/pi/Mpu-Webui/mpu')
import MPU6050
gyro = [0]*3
mpu = MPU6050.MPU6050()
mpu.dmp_initialize()

while True:
    gyro = mpu.get_rotation()
    gyro = str(gyro)
    f = open("static/rpy.txt", "w")
    f.write(gyro)
    f.close()
    time.sleep(0.1)
    print(gyro)
