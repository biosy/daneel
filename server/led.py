#!/usr/bin/env python
import RPi.GPIO as GP
import time

class Led:
    def __init__(self, pin):
        self.pin = pin
        GP.setmode(GP.BOARD)
        GP.setup(self.pin, GP.OUT)
        self.type = "output"

    def led_on(self):
        GP.output(self.pin, GP.HIGH)

    def led_off(self):
        GP.output(self.pin, GP.LOW)

    def set_status(self, status):
        if status == "on":
            self.led_on()

        elif status == "off":
            self.led_off()

led = Led(11)

