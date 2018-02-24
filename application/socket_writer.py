import socket
from application.socket_listener import *
from application.ping_request import *

class SocketWriter:
    def __init__(self, addrs, port):
        self.addr = addrs
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        print(self.addr + str(self.port))
        self.socket.connect((self.addr,self.port))
        print("connected")

    def send(self, message):
        self.socket.send((message.encapsulate()+"\r").encode("utf-8"))
        print(message.encapsulate().encode("utf-8"))


def on_message(message):
    print(message)









