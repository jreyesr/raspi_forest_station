#!/usr/bin/env python3

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN)

GPIO.wait_for_edge(24, GPIO.RISING)
print("Rising edge detected!")
GPIO.wait_for_edge(24, GPIO.FALLING)
print("Falling edge detected")

GPIO.cleanup()
