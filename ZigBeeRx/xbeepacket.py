import pandas as pd
from threading import Timer
from digi.xbee.devices import XBeeMessage
import sys

class XBeePacket:
    def __init__(self, packet: XBeeMessage, csv_file='../RxData.csv'):
        self.csv_file = csv_file
        self.packet = packet
        self.remote_device = self.packet.remote_device
        self.data = self.packet.data
        self.timestamp = self.packet.timestamp

    def to_dict(self):
        return self.packet.to_dict()













