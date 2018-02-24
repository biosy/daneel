from application.socket_listener import *
from application.socket_writer import *
from server.device_manager import *
from server.button import *
from application.croom_message import *
from application.data import *
from application.data_change import *
from application.command_request import*
from application.socket_writer import *
from server.hearbeat_sensors import *
from server.led import Led
import time
from application.serial_receiver import SerialReceiver

class Client:
    def __init__(self, port):
        # Declare socketListener to communicate with client
        # Just listen to a given port
        self.listener = SocketListener(port, self.on_message)
        self.listener.start()
        self.writer = None
        self.server_name = ""
        self.state = 0
        self.is_connected = False # True if we are connected to the controller

        # Welcome display
        print("Welcome to the DANELL displaying mode\n\n", end ='')

        print("Waiting for connection", end ='')

        while self.is_connected == False:
            try:
                self.serial = SerialReceiver(self.on_control,9600,"/dev/ttyACM0")
                self.serial.start()
                self.is_connected = True
                print('\nconnected to the controller')

            except:
                print('.', end='', flush=True)

            time.sleep(1)

        # Ping all components on arduino
        hb = HeartbeatSensors(self.serial)
        hb.start()


    def on_message(self, message):
        # Start to interpret as a generic message
        primal_message = CroomMessage("","")
        primal_message.decapsulate(message.decode("utf-8"))
        print(primal_message.msgid)
        # Case : data message
        if primal_message.msgid == "04":
            secondal_message = Data("")
            secondal_message.decapsulate(message.decode("utf-8"))
            #self.server_name = secondal_message.data
    
        if primal_message.msgid =="05":
            secondal_message = CommandRequest("","")
            secondal_message.decapsulate(message.decode("utf-8"))
            if secondal_message.cmdId == "01":
                self.server_name = secondal_message.data
                print("request from : ", end='', flush = True)
                print(self.server_name)
                self.server = SocketWriter(self.server_name, 5000)
                self.server.connect()
            print(secondal_message.cmdId)
            print("ok?")
        # Case : data exchange
        if primal_message.msgid == "03":
            secondal_message = DataChange("","")
            secondal_message.decapsulate(message.decode("utf-8"))

            # case led
            if(secondal_message.deviceName == "led"):
                # case led on
                if secondal_message.value == "01":

                    self.serial.send_string(b'l')
                # case led off
                if secondal_message.value =="02":

                    self.serial.send_string(b'o')

        
    def on_control(self, message):
        #print(message)
        print("receved")
        try:
            split = message.decode("utf-8").split('/')
            split[1]=split[1].replace('\r\n', '')
            print(split)
            secondal_message = DataChange(str(split[0]),str(split[1]))
            if self.server_name != "":
                try:
                    self.server.send(secondal_message)
                except:
                    print("zozoé")
                pass
        except:
            raise Exception()
            pass
  



cli = Client(5001)

