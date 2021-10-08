import RPi.GPIO as GPIO

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

GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# loop
if __name__ == '__main__':
    print("Ctrl + C to exit")
    try:
        while 1:
            if GPIO.input(btn):
                GPIO.output(led1, GPIO.HIGH)
                GPIO.output(led2, GPIO.LOW)
            else:
                GPIO.output(led1, GPIO.LOW)
                GPIO.output(led2, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(led2, GPIO.LOW)
                time.sleep(0.1)

    except KeyboardInterrupt:
        GPIO.cleanup()








