import time

from setup import *
import RPi.GPIO as GPIO

def capture_normal():
    GPIO.output(led_White, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_White, GPIO.LOW)

def capture_UV():
    GPIO.output(led_UV, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_UV, GPIO.LOW)

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
    time.sleep(0.5)


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


def button_pressed_callback(channel):
    global state
    if state == 0:
        detect_blood()
        print("detect blood!")
    elif state == 1:
        detect_stain()
        print("detect stain!")
    else:
        pass

