import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

#Set GPIO Pin 21 as Input, and set an internal Pull-Down Resistor 
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    print("Starting GPIO Test from MSP430 to RPi...")
    while True:
        if(GPIO.input(21)):
            print("GPIO is High")
        else:
            print("GPIO is Low")
            
finally:
    print("Exiting GPIO Test...")
    GPIO.cleanup()