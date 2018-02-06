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
        #button = Button("test",)
        #self.board.add_button()
        self.led = Led(7)
        self.led.led_off()
        self.state = 0
        self.led_state = Led(11)
        self.led_state.led_off()
    def on_message(self, message):
        primal_message = CroomMessage("","")
        primal_message.decapsulate(message.decode("utf-8"))
        print(primal_message.msgid+"\n")
        if primal_message.msgid == "04":
            print("ok")
            secondal_message = Data("")
            secondal_message.decapsulate(message.decode("utf-8"))
            self.server_name = secondal_message.data
            #self.writer = SocketWriter(self.server_name,5000)
            print("ok\n")
            self.led_state.led_on()
            time.sleep(0.1)
            self.led_state.led_off()
            time.sleep(0.1)
            self.led_state.led_on()
            time.sleep(0.1)
            self.led_state.led_off()
            time.sleep(0.1)
            self.led_state.led_on()

        if primal_message.msgid == "03":
            print("you\n")
            secondal_message = DataChange("","")
            secondal_message.decapsulate(message.decode("utf-8"))

            if(secondal_message.deviceName == "led"):
                if secondal_message.value == "01":
                    self.led.led_on()      
                    print("again")

                if secondal_message.value =="02":
                    self.led.led_off()

cli = Client(5001)

