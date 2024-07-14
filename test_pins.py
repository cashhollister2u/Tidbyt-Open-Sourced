import RPi.GPIO as GPIO
import time

pin_test = int(input("type pin to test: "))
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin_test,GPIO.OUT)
print( "LED on")
GPIO.output(pin_test,GPIO.HIGH)
time.sleep(1)
print( "LED off")
GPIO.output(pin_test,GPIO.LOW)
