import RPi.GPIO as GPIO

led1 = 18 # P1 pin 12
led2 = 23 # P1 pin 16
btn  = 17 # P1 pin 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Ctrl + C to exit")
try:
    while 1:
        if GPIO.input(btn):
            GPIO.output(led1, GPIO.HIGH)
