#!/usr/bin/env python
import os


class Camera:
    """
        This class is the main camera reader
        Only get by frame at a specific instant
        We don't a continuous reader
    """
    def __init__(self):
        self.list_serials = []
        self.find_serial()
        self.default = self.list_serials[0]
        self.type = "input"

    def find_serial(self):
        """
            find all serials ports
        """
        list_files = os.listdir("/dev")
        for file in list_files:
            if "ttyUSB" in file or "ttyACM" in file or "video" in file:
                self.list_serials.append(file)

    def get_frame(self):
        pass


