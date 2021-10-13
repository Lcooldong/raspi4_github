import signal
import sys
import RPi.GPIO as GPIO
import time

from function import *

state = 0
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

last_ledGreen_state = 0
count = 0
def button_pressed_callback(channel):
    global state
    detect_blood()
    print("detect blood!")



# MAIN LOOP
if __name__ == '__main__':
    try:
        GPIO.add_event_detect(btn1, GPIO.RISING, callback=button_pressed_callback, bouncetime=1000)
        #signal.signal(signal.SIGINT, signal_handler)
        #signal.pause()

    except KeyboardInterrupt:
        print("error")
        GPIO.cleanup()

    finally:
        GPIO.cleanup()