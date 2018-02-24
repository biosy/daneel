import socket
import threading
import time

class HeartbeatSensors(threading.Thread):
    def __init__(self,  serial):
        self.serial = serial
        self.stop_event = False
        threading.Thread.__init__(self)  # ne pas oublier cette ligne

    def run(self):
        while not self.stop_event:
            time.sleep(1)
            self.serial.send_string(b't')
            time.sleep(0.1)
            self.serial.send_string(b'u')
            time.sleep(0.1)
            self.serial.send_string(b'b')
            time.sleep(0.1)


    def close(self):
        self.stop_event = True




