import RPi.GPIO as GPIO
import time

SERVO_PIN = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)

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