import RPi.GPIO as GPIO
import time
from setup import *


def start_program():
    GPIO.output(vibrator, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(vibrator, GPIO.LOW)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(buzzer, GPIO.LOW)

def detect_blood():
    GPIO.output(led_Green, GPIO.HIGH)
    GPIO.output(vibrator, GPIO.HIGH)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(vibrator, GPIO.LOW)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(vibrator, GPIO.HIGH)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(vibrator, GPIO.LOW)
    GPIO.output(buzzer, GPIO.LOW)
    GPIO.output(led_Green, GPIO.LOW)

def detect_stain():
    GPIO.output(led_Blue, GPIO.HIGH)
    GPIO.output(vibrator, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(vibrator, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(vibrator, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(vibrator, GPIO.LOW)
    GPIO.output(led_Blue, GPIO.LOW)