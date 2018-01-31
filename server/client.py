from application.socket_listener import *
from application.socket_writer import *
from server.device_manager import *
from server.button import *
from application.croom_message import *
from application.data import *

class Client:
    def __init__(self, port):
        self.listener = SocketListener(port, self.on_message)
        self.listener.start()
        self.writer = None
        self.server_name = ""
        self.board = DeviceManager()
        button = Button("test",)
        self.board.add_button()
    def on_message(self, message):
        primal_message = CroomMessage("","")
        primal_message.decapsulate(message)

        if primal_message.msgid == "04":
            secondal_message = Data("")
            secondal_message.decapsulate(message)
            self.server_name = secondal_message.data
            self.writer = SocketWriter(self.server_name,5000)



cli = Client(5001)

