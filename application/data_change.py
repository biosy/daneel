import application.croom_message as cr
import json


class DataChange(cr.CroomMessage):
    """
    Define command data


    """

    def __init__(self, deviceName, value):
        cr.CroomMessage.__init__(self, "03", {"deviceName": deviceName, "value": value})
        self.deviceName = deviceName
        self.value = value

    def encapsulate(self):
        return json.dumps({"msgid": "03", "payload": {"deviceName": self.deviceName, "value": self.value}})

    def decapsulate(self, str):
        json_parsed = json.loads(str)
        self.msgid = json_parsed["msgid"]
        self.deviceName = json_parsed["payload"]["deviceName"]
        self.value = json_parsed["payload"]["value"]
        self.payload = json_parsed["payload"]
        pass

    def print(self):
        print("print data request \n\n")
        print("msgid : " + self.msgid + "\n")
        print("payload : " + json.dumps(self.payload) + "\n")
        print("deviceName : " + self.deviceName + "\n")
        print("value : " + self.value + "\n")
