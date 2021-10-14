import signal
import sys
import RPi.GPIO as GPIO
from function import *


# MAIN LOOP
if __name__ == '__main__':
    try:
        start_program()
        GPIO.add_event_detect(btn1, GPIO.RISING, callback=button_pressed_callback, bouncetime=5000)
        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()

    except KeyboardInterrupt:
        print("error")

    finally:
        pass
        #GPIO.cleanup()
