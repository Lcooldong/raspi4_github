import signal
import sys
import RPi.GPIO as GPIO
import time

btn1 = 18
led_Blue = 22
led_Green = 27
led_Red = 17


last_ledGreen_state = 0
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_Blue, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_Green, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_Red, GPIO.OUT, initial=GPIO.LOW)

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def button_pressed_callback1(channel):
    global last_ledGreen_state
    global count
    GPIO.output(led_Green, not last_ledGreen_state)
    last_ledGreen_state = not last_ledGreen_state
    #print("btn1")
    count += 1
    print(count)


if __name__ == '__main__':
    try:
        while True:
            GPIO.output(led_Red, GPIO.LOW)
            GPIO.output(led_Green, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(led_Green, GPIO.LOW)
            GPIO.output(led_Blue, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(led_Blue, GPIO.LOW)
            GPIO.output(led_Red, GPIO.HIGH)
            time.sleep(0.5)


        GPIO.add_event_detect(btn1, GPIO.RISING, callback=button_pressed_callback1, bouncetime=1000)
        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()

    except KeyboardInterrupt:
        print("error")
        GPIO.cleanup()

    finally:
        GPIO.cleanup()