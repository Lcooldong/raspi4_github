import RPi.GPIO as GPIO
import time

whiteLed = 17  # GPIO17
UVLed = 18     # GPIO18
vibrator = 23  # GPIO23
buzzer = 24    # GPIO24
btn1 = 27      # GPIO27
btn2 = 22      # GPIO22
ledGreen = 5   # GPIO_5
ledRed = 6     # GPIO_6

# setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(whiteLed, GPIO.OUT)
GPIO.setup(UVLed, GPIO.OUT)
GPIO.setup(vibrator, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledRed, GPIO.OUT)

GPIO.setup(btn1, GPIO.IN, GPIO.LOW)
GPIO.setup(btn2, GPIO.IN, GPIO.LOW)

#GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# loop
if __name__ == '__main__':
    print("Ctrl + C to exit")
    try:
        while True:
            if GPIO.input(btn1):
                print("btn1")
                time.sleep(0.5)
            else:
                GPIO.output(UVLed, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(UVLed, GPIO.LOW)
                time.sleep(0.1)

            if GPIO.input(btn2):
                print("btn2")
                time.sleep(0.5)

    except KeyboardInterrupt:
        GPIO.cleanup()








