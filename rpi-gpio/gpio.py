#!/usr/bin/python

import RPi.GPIO as GPIO
import time
#import logging

#logging.basicConfig(format='%(levelname)s-%(asctime)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG,filename='/App/gpio.log')

# Set GPIO mode: GPIO.BCM or GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# Set mode for each gpio pin
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)

while True:
	# Get value from light sensor - gpio 17 
	is_light_on = GPIO.input(17)
	print("Is light on ? " + is_light_on)
	time.sleep(1)

# Reset all gpio pin
GPIO.cleanup()