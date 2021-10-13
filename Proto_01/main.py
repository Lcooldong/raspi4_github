import signal
import sys
import RPi.GPIO as GPIO
import time

#INPUT
btn1 = 18

#RGB
led_Blue = 22
led_Green = 27
led_Red = 17

#Peripheral
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


last_ledGreen_state = 0
count = 0

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def button_pressed_callback(channel):
    global last_ledGreen_state
    global count
    GPIO.output(led_Green, not last_ledGreen_state)
    last_ledGreen_state = not last_ledGreen_state
    #print("btn1")
    count += 1
    print(count)

    if count == 2:
        GPIO.output(buzzer, GPIO.HIGH)
    elif count == 4:
        GPIO.output(vibrator, GPIO.HIGH)
    else:
        GPIO.output(buzzer, GPIO.LOW)
        GPIO.output(vibrator, GPIO.LOW)

# MAIN LOOP
if __name__ == '__main__':
    try:
        GPIO.add_event_detect(btn1, GPIO.RISING, callback=button_pressed_callback, bouncetime=1000)
        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()

    except KeyboardInterrupt:
        print("error")
        GPIO.cleanup()

    finally:
        GPIO.cleanup()