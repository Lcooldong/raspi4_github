import sys
import RPi.GPIO as GPIO
import time

# INPUT
btn1 = 18

# RGB
led_Blue = 22
led_Green = 27
led_Red = 17

# Peripheral
led_UV = 12
led_White = 16
vibrator = 20
buzzer = 21

# SETUP
GPIO.setmode(GPIO.BCM)

GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(led_Blue, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_Green, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_Red, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(led_UV, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_White, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(vibrator, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.LOW)


def start_program():
    GPIO.output(vibrator, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(vibrator, GPIO.LOW)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(buzzer, GPIO.LOW)


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)