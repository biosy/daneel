import socket
import threading

class SocketListener(threading.Thread):
    def __init__(self,  port, on_message):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(("", self.port))
        self.socket.listen(5)
        self.stop_event = False
        self.on_message = on_message
        threading.Thread.__init__(self)  # ne pas oublier cette ligne

    def run(self):
        self.connection, self.client_address = self.socket.accept()
        print("connected")
        while not self.stop_event:
            data = self.connection.recv(100)
            self.on_message(data)

    def close(self):
        self.stop_event = True




