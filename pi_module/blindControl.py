import RPi.GPIO as GPIO
import time
import smbus
import threading
import time
import test

I2C_CH = 1
BH1750_DEV_ADDR = 0x23

CONT_H_RES_MODE     = 0x10
CONT_H_RES_MODE2    = 0x11
CONT_L_RES_MODE     = 0x13
ONETIME_H_RES_MODE  = 0x20
ONETIME_H_RES_MODE2 = 0x21
ONETIME_L_RES_MODE  = 0x23

SERVO_PIN = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)

def readIlluminance():
    i2c = smbus.SMBus(I2C_CH)
    luxBytes = i2c.read_i2c_block_data(BH1750_DEV_ADDR, CONT_H_RES_MODE, 2)
    lux = int.from_bytes(luxBytes, byteorder='big')
    i2c.close()
    return lux

def blindAuto():
    while True:
        x = readIlluminance()
        print('{0} lux'.format(x))

        if x > 50:
            blindRaise()
        else:
            blindLower()
        
        time.sleep(1)

def blindRaise():
    servo.ChangeDutyCycle(11.5)
    time.sleep(2)
    

def blindLower():
    servo.ChangeDutyCycle(1.5)
    time.sleep(2)

def auto():
    try:
        while True:
            blindRaise()
            blindLower()

    except KeyboardInterrupt:  
        servo.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    blindLower()
    blindRaise()
    blindAuto()