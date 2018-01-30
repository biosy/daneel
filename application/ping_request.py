import application.croom_message as cr
import json

class PingRequest(cr.CroomMessage):
    """
    Define ping request
    """
    def __init__(self):
        cr.CroomMessage.__init__(self,"01", {})

    def encapsulate(self):
        return json.dumps({"msgid":"01", "payload":{}})

    def decapsulate(self, str):
        json_parsed = json.loads(str)
        self.msgid = json_parsed["msgid"]
        self.payload = json_parsed["payload"]
        pass

    def print(self):
        print("print cmdRequest \n\n")
        print("msgid : "+self.msgid + "\n")
        print("payload : "+json.dumps(self.payload) + "\n")
