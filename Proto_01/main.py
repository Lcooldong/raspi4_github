import signal
import sys
import RPi.GPIO as GPIO
import time

from function import *


state = 0
def button_pressed_callback(channel):
    global state
    if state == 0:
        detect_blood()
    elif state == 1:
        detect_stain()
    else:
        GPIO.output(led_White, GPIO.HIGH)


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