from application.socket_listener import *
from application.socket_writer import *
from server.device_manager import *
from server.button import *
from application.croom_message import *
from application.data import *
from application.data_change import *
from server.led import Led
import time
from application.serial_receiver import SerialReceiver

class Client:
    def __init__(self, port):
        self.listener = SocketListener(port, self.on_message)
        self.listener.start()
        self.writer = None
        self.server_name = ""
        self.led.led_off()
        self.state = 0
        self.serial = SerialReceiver(self.on_control,9600,"/dev/ttyACM0")

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
                    self.serial.send("LED")
                # case led off
                if secondal_message.value =="02":
                    self.serial.send("LEO")

    def on_control(self, message):
        print(message)
        pass

cli = Client(5001)

