import signal
import sys
import RPi.GPIO as GPIO

btn1 = 8
btn2 = 8
ledGreen = 5
ledRed = 6

last_ledGreen_state = 0
last_ledRed_state = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1, GPIO.IN)
GPIO.setup(btn2, GPIO.IN)
GPIO.setup(ledGreen, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ledRed, GPIO.OUT, initial=GPIO.LOW)

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def button_pressed_callback1(channel):
    global last_ledGreen_state
    GPIO.output(ledGreen, not last_ledGreen_state)
    last_ledGreen_state = not last_ledGreen_state

def button_pressed_callback2(channel):
    global last_ledRed_state
    GPIO.output(ledRed, not last_ledRed_state)
    last_ledRed_state = not last_ledRed_state

if __name__ == '__main__':
    try:
        GPIO.add_event_detect(btn1, GPIO.RISING, callback=button_pressed_callback1, bouncetime=200)
        #GPIO.add_event_detect(btn2, GPIO.RISING, callback=button_pressed_callback2, bouncetime=200)
        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()
    except:
        print("error")

    finally:
        GPIO.cleanup()