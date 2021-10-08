import RPi.GPIO as GPIO
import time

whiteLed = 17  # GPIO17
UVLed = 18     # GPIO18
vibrator = 23  # GPIO23
buzzer = 24    # GPIO24
btn1 = 8      # GPIO27
btn2 = 7      # GPIO22
ledGreen = 5   # GPIO_5
ledRed = 6     # GPIO_6

# setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(whiteLed, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(UVLed, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(vibrator, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ledGreen, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ledRed, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(btn1, GPIO.IN)
GPIO.setup(btn2, GPIO.IN)

def btn1pushed(channel):
    print("button1")

def btn2pushed(channel):
    print("button2")

# loop
if __name__ == '__main__':
    print("Ctrl + C to exit")
    try:
        GPIO.add_event_detect(btn1, GPIO.RISING, callback=btn1pushed, bouncetime=200)
        GPIO.add_event_detect(btn2, GPIO.RISING, callback=btn2pushed, bouncetime=200)

        # while True:
        #     pass

    except:
        print("error")
    finally:
        GPIO.remove_event_detect(btn1)
        GPIO.remove_event_detect(btn2)
        GPIO.cleanup()
