import signal
import sys
import RPi.GPIO as GPIO
import time

btn1 = 8
btn2 = 7
vibrator = 23  # GPIO23
buzzer = 24    # GPIO24
ledGreen = 6
ledRed = 5

last_ledGreen_state = 0
last_ledRed_state = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(vibrator, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ledGreen, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ledRed, GPIO.OUT, initial=GPIO.LOW)

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def button_pressed_callback1(channel):
    global last_ledGreen_state
    GPIO.output(ledGreen, not last_ledGreen_state)
    last_ledGreen_state = not last_ledGreen_state
    GPIO.output(vibrator, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(vibrator, GPIO.LOW)

def button_pressed_callback2(channel):
    global last_ledRed_state
    GPIO.output(ledRed, not last_ledRed_state)
    last_ledRed_state = not last_ledRed_state
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(buzzer, GPIO.LOW)

if __name__ == '__main__':
    try:
        GPIO.add_event_detect(btn1, GPIO.RISING, callback=button_pressed_callback1, bouncetime=500)
        GPIO.add_event_detect(btn2, GPIO.RISING, callback=button_pressed_callback2, bouncetime=500)
        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()

    except KeyboardInterrupt:
        print("error")
        GPIO.cleanup()

    finally:
        GPIO.cleanup()