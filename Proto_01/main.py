import signal
import sys
import RPi.GPIO as GPIO
import time

from function import *


def button_pressed_callback(channel):
    detect_blood()
    print("detect blood!")


# MAIN LOOP
if __name__ == '__main__':
    try:
        #start_program()

        GPIO.add_event_detect(btn1, GPIO.RISING, callback=button_pressed_callback, bouncetime=1000)
        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()

    except KeyboardInterrupt:
        print("error")
        GPIO.cleanup()

    finally:
        GPIO.cleanup()