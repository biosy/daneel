import socket
from application.socket_listener import *
from application.ping_request import *

class SocketWriter:
    def __init__(self, addrs, port):
        self.addr = addrs
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.connect((self.addr,self.port))

    def send(self, message):
        self.socket.send(message.encapsulate().encode("utf-8"))


def on_message(message):
    print(message)









