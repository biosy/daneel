from application.serial_receiver import *
import os
from application.socket_listener import *
from application.socket_writer import *
from application.data import *

class Board:
    """
    This class contains all informations about the device
    """

    def __init__(self):
        self.serial = None
        self.socketListener = None
        self.wifi_connected = False

    def connect_to_serial(self, addr, baudrate):
        self.serial = SerialReceiver(self.on_message, baudrate, addr)

    def on_message(self, message):
        print(message)

    def find_serials(self):
        list_files = os.listdir("/dev")
        list_serials = []
        for file in list_files:
            if "ttyUSB" in file or "ttyACM" in file or "video" in file:
                list_serials.append("/dev/"+file)

        return list_serials

    def connect_to_wifi(self, addr, port):
        if self.wifi_connected == False:
            try:
                data = Data("192.168.0.11:5000")
                self.socketWriter = SocketWriter(addr,port)
                self.wifi_connected = True
                self.socketListener = SocketListener(5000,self.on_message)
                self.socketListener.start()
                self.socketWriter.send(data.encapsulate())

            except:
                self.wifi_connected = False

        else :
            # disconnection
            self.wifi_connected = False
            self.socketListener.close()
