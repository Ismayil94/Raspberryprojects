import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

LED = GPIO.PWM(7,100)

LED.start(0)

pause_time = 0.05

try:
    while True:
        for i in range(0,101):

            LED.ChangeDutyCycle(100-i)
            time.sleep(pause_time)
            
        for i in range(100,-1,-1):

            LED.ChangeDutyCycle(100-i)
            time.sleep(pause_time)

except KeyboardInterrupt:
       LED.stop()
