import json

class CroomMessage:
    """
    This class use to define message to send to the device
    """

    def __init__(self, msgid, payload):
        self.msgid = msgid
        self.payload = payload

    def encapsulate(self):
        return json.dumps({"msgid":self.msgid, "payload":self.payload}, sort_keys=True)

    def decapsulate(self, str):
        json_parsed = json.load(str)
        self.msgid = json_parsed["msgid"]
        self.payload = json_parsed["payload"]

    def print(self):
        print("msgid : " + self.msgid +"\npayload : " + self.payload)
        
