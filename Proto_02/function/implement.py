# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import numpy as np
import cv2
import os
import time

from setup import *


count = 0
def capture():
    global count
    cap = cv2.VideoCapture(0, cv2.CAP_V4L)  # 노트북 웹캠을 카메라로 사용
    cap.set(3, 640)  # 너비
    cap.set(4, 480)  # 높이

    ret, frame = cap.read()  # 사진 촬영
    frame = cv2.flip(frame, 1)  # 좌우 대칭

    #    print(os.path.dirname(os.path.realpath(__file__)))
    count += 1
    filename = str(count) + '.jpg'
    cv2.imwrite('./Proto_02/picture/' + filename, frame)  # 사진 저장

    cap.release()
    cv2.destroyAllWindows()


def capture_white_Led():
    GPIO.output(led_White, GPIO.HIGH)
    capture()
    time.sleep(0.1)
    GPIO.output(led_White, GPIO.LOW)

def capture_UV_Led():
    GPIO.output(led_UV, GPIO.HIGH)
    capture()
    time.sleep(0.1)
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


def detect_error():
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.LOW)

state = 0
def button_pressed_callback(channel):
    global state
    capture_white_Led()
    capture_UV_Led()
    if state == 2:
        detect_blood()
        print("detect blood!")
    elif state == 1:
        detect_stain()
        print("detect stain!")
    else:
        detect_error()

