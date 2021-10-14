import time
import numpy as np
import cv2
from setup import *
import RPi.GPIO as GPIO

count = 0
def capture():
    global count
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.imwrite('./picture/1.jpg', frame)
    count += 1
    cap.release()
    cv2.destroyAllWindows()

def capture_white_Led():
    GPIO.output(led_White, GPIO.HIGH)
    capture()
    time.sleep(1)
    GPIO.output(led_White, GPIO.LOW)

def capture_UV_Led():
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

state = 0
def button_pressed_callback(channel):
    global state
    capture_white_Led()
    capture_UV_Led()
    if state == 0:
        detect_blood()
        print("detect blood!")
    elif state == 1:
        detect_stain()
        print("detect stain!")
    else:
        pass

