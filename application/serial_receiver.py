import serial
import threading

class SerialReceiver(threading.Thread):
    def __init__(self, on_message, baudrate=9600, port = '/dev/ttyUSB0'):
        self.ser = serial.Serial(port=port, baudrate=baudrate, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
        self.baudrate = baudrate
        self.port = port
        self.stop_event = False
        self.on_message = on_message
        threading.Thread.__init__(self)

    def send(self, message):
        self.ser.write(message.encapsulate)

    def send_string(self, message):
        self.ser.write(message)

    def run(self):
        while not self.stop_event:
            buffer = self.ser.readline()
            self.on_message(buffer)

