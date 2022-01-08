#!/usr/bin/env python3
import MPU6050
import time

mpu = MPU6050.MPU6050()     # instantiate a MPU6050 class object
accel = [0]*3               # define an arry to store accelerometer data
gyro = [0]*3
        # define an arry to store gyroscope data

def setup():
    mpu.dmp_initialize()    # initialize MPU6050

x = 0    

def loop():
    while(True):
        global gyro
        accel = mpu.get_acceleration()      # get accelerometer data
        gyro = mpu.get_rotation()           # get gyroscope data
#        print("a/g:%d\t%d\t%d\t%d\t%d\t%d "%(accel[0],accel[1],accel[2],gyro[0],gyro[1],gyro[2]))
#        print("a/g:%.2f g\t%.2f g\t%.2f g\t%.2f d/s\t%.2f d/s\t%.2f d/s"%(accel[0]/16384.0,accel[1]/16384.0,
#            accel[2]/16384.0,gyro[0]/131.0,gyro[1]/131.0,gyro[2]/131.0))
#        print(gyro[0])
#        print(accel)
#        print("sending")
#        setgyro(tmpgyro)
#        print(getgyro())
#        print("["+tmpgyro[0]+",")
#        print(tmpgyro[1]+",")
#        print(tmpgyro[2]+"]")
#        print(tmpgyro)
        setgyro(gyro)
        getgyro()
        time.sleep(0.1)
def setgyro(g):
    global gyro
    gyro = g
def getgyro():
    global gyro
    print(gyro)
    return gyro


if __name__ == '__main__':     # Program entrance
    print("Program is starting ... ")
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass

