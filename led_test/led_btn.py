import RPi.GPIO as GPIO

led1 = 18 # P1 pin 12
led2 = 23 # P1 pin 16
btn1  = 24 # P1 pin 11
btn2  = 25 # P1 pin 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
