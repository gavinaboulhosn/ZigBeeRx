import threading
import time
import serial
from ZigBeeRx.RxController import RxController
from ZigBeeRx.xbeepacket import XBeePacket


class RxThread(threading.Thread):
    def __init__(self, controller: RxController, packet: XBeePacket, name="RXReceive"):
        threading.Thread.__init__(self)
        self.name = name
        self.controller = controller
        self.packet = packet
        self.timeout = 10
        self.reset_count = 0

    def run(self):
        while self.controller.is_open():
            try:
                self.controller.receive_from()
                self.reset_count = 0
            except serial.SerialException:
                time.sleep(1)
                self.reset_count += 1
                if self.reset_count > self.timeout:
                    self.controller.disconnect()
                    return




