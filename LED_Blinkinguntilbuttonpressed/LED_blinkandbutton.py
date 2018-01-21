import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13, GPIO.OUT)

def blink():
    GPIO.output(13,True)
    time.sleep(0.5)
    GPIO.output(13,False)
    time.sleep(0.5)
    
while True:
    if GPIO.input(11) == True:
        GPIO.output(13,True)
    elif GPIO.input(11) == False:
        blink()
