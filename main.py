import logging
import RPi.GPIO as GPIO

from ultrasound import *

# Configure Logger
FORMAT = "[%(levelname)s] %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
# Set pin values for ultrasound location
TRIG = 23
ECHO = 24

distance = ultrasound_ping(TRIG, ECHO)
print("Distance: {} cm".format(distance))
