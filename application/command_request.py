import application.croom_message as cr
import json

class CommandRequest(cr.CroomMessage):
    """
    Define command data


    """
    def __init__(self, cmdId, data):
        cr.CroomMessage.__init__(self,"05", {"cmdId":cmdId, "data": data})
        self.cmdId = cmdId
        self.data = data


    def encapsulate(self):
        return json.dumps({"msgid":"5", "payload":{"cmdId": self.cmdId, "data": self.data}})

    def decapsulate(self, str):
        json_parsed = json.loads(str)
        self.msgid = json_parsed["msgid"]
        self.cmdId = json_parsed["payload"]["cmdId"]
        self.data = json_parsed["payload"]["data"]
        self.payload = json_parsed["payload"]
        pass

    def print(self):
        print("print cmdRequest \n\n")
        print("msgid : "+self.msgid + "\n")
        print("payload : "+json.dumps(self.payload) + "\n")
        print("cmdId : "+self.cmdId+ "\n")
        print("data : "+self.data + "\n")
