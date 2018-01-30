import application.croom_message as cr
import json


class Data(cr.CroomMessage):
    """
    Define command data


    """

    def __init__(self, data):
        cr.CroomMessage.__init__(self, "04", {"data": data})
        self.data = data

    def encapsulate(self):
        return json.dumps({"msgid": "04", "payload": {"data": self.data}})

    def decapsulate(self, str):
        json_parsed = json.loads(str)
        self.msgid = json_parsed["msgid"]
        self.data = json_parsed["payload"]["data"]
        self.payload = json_parsed["payload"]
        pass

    def print(self):
        print("print data request \n\n")
        print("msgid : " + self.msgid + "\n")
        print("payload : " + json.dumps(self.payload) + "\n")
        print("data : " + self.data + "\n")
