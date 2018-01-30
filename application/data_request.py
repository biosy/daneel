import application.croom_message as cr
import json


class DataRequest(cr.CroomMessage):
    """
    Define command data


    """

    def __init__(self, deviceName, option):
        cr.CroomMessage.__init__(self, "02", {"deviceName": deviceName, "option": option})
        self.deviceName = deviceName
        self.option = option

    def encapsulate(self):
        return json.dumps({"msgid": "02", "payload": {"deviceName": self.deviceName, "option": self.option}})

    def decapsulate(self, str):
        json_parsed = json.loads(str)
        self.msgid = json_parsed["msgid"]
        self.deviceName = json_parsed["payload"]["deviceName"]
        self.option = json_parsed["payload"]["option"]
        self.payload = json_parsed["payload"]
        pass

    def print(self):
        print("print data request \n\n")
        print("msgid : " + self.msgid + "\n")
        print("payload : " + json.dumps(self.payload) + "\n")
        print("deviceName : " + self.deviceName + "\n")
        print("option : " + self.option + "\n")
