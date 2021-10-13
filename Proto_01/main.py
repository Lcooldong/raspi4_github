import signal
import sys
import RPi.GPIO as GPIO


from function import *

state = 0

last_ledGreen_state = 0
count = 0
def button_pressed_callback(channel):
    global state
    if state == 0:
        detect_blood()
    elif state == 1:
        pass
    else:
        pass
    print("detect blood!")



# MAIN LOOP
if __name__ == '__main__':
    try:
        GPIO.add_event_detect(btn1, GPIO.RISING, callback=button_pressed_callback, bouncetime=5000)
        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()

    except KeyboardInterrupt:
        print("error")
        GPIO.cleanup()

    finally:
        GPIO.cleanup()