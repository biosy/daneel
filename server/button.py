#!/usr/bin/env python
import threading
import RPi.GPIO as  GPIO

class Button(threading.Thread):
    def __init__(self, name, pin, callback):
        threading.Thread.__init__(self)
        self.name = name
        self.pin = pin
        self.callback = callback
        self.stop_event = False
        self.type = "input"

    def run(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        while not self.stop_event:
            button = GPIO.input(self.pin)
            self.callback(button)





