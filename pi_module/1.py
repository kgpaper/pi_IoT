import RPi.GPIO as GPIO
import time

SERVO_PIN = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)
servo.ChangeDutyCycle(11.5)
time.sleep(1)
servo.stop()
GPIO.cleanup()