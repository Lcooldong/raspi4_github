import signal
import sys
import RPi.GPIO as GPIO
import time

btn1 = 18
led = 17

last_ledGreen_state = 0
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def button_pressed_callback1(channel):
    global last_ledGreen_state
    global count
    GPIO.output(led, not last_ledGreen_state)
    last_ledGreen_state = not last_ledGreen_state
    #print("btn1")
    count += 1
    print(count)


if __name__ == '__main__':
    try:
        GPIO.add_event_detect(btn1, GPIO.RISING, callback=button_pressed_callback1, bouncetime=1000)
        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()

    except KeyboardInterrupt:
        print("error")
        GPIO.cleanup()

    finally:
        GPIO.cleanup()