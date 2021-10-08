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

btn1State = False
lastBtn1State = False
btn2State = False
lastBtn2State = False


# loop
if __name__ == '__main__':
    print("Ctrl + C to exit")
    try:
        while True:
            btn1State = GPIO.input(btn1)
            btn2State = GPIO.input(btn2)

            if (btn1State != lastBtn1State):
                print("btn1")
                GPIO.output(ledGreen, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(ledGreen, GPIO.LOW)

            if (btn2State != lastBtn2State):
                print("btn2")
                GPIO.output(ledRed, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(ledRed, GPIO.LOW)

            if (btn1State == True):
                GPIO.output(whiteLed, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(whiteLed, GPIO.LOW)
                time.sleep(0.5)

            lastBtn1State = btn1State
            lastBtn2State = btn2State

    except:
        print("error")
    finally:
        GPIO.cleanup()
