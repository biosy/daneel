from application.socket_listener import *
from application.socket_writer import *
from server.device_manager import *
from server.button import *
from application.croom_message import *
from application.data import *
from application.data_change import *
from server.led import Led
import time

class Client:
    def __init__(self, port):
        self.listener = SocketListener(port, self.on_message)
        self.listener.start()
        self.writer = None
        self.server_name = ""
        self.board = DeviceManager()
        self.led = Led(7)
        self.led.led_off()
        self.state = 0
        self.led_state = Led(11)
        self.led_state.led_off()
    def on_message(self, message):
        # Start to interpret as a generic message
        primal_message = CroomMessage("","")
        primal_message.decapsulate(message.decode("utf-8"))

        # Case : data message
        if primal_message.msgid == "04":
            secondal_message = Data("")
            secondal_message.decapsulate(message.decode("utf-8"))
            self.server_name = secondal_message.data

        # Case : data exchange
        if primal_message.msgid == "03":
            secondal_message = DataChange("","")
            secondal_message.decapsulate(message.decode("utf-8"))

            # case led
            if(secondal_message.deviceName == "led"):
                # case led on
                if secondal_message.value == "01":
                    self.led.led_on()      
                    print("again")

                # case led off
                if secondal_message.value =="02":
                    self.led.led_off()

cli = Client(5001)

