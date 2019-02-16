import threading
import time
import serial
from ZigBeeRx.RxController import RxController
from ZigBeeRx.xbeepacket import XBeePacket

class TxThread(threading.Thread):
    def __init__(self, controller: RxController, packet: XBeePacket, name="TX"):
        threading.Thread.__init__(self)
        self.name = name
        self.controller = controller
        self.packet = packet
        self.timeout = 10

    def run(self):
        self.update_count = 0
        self.reset_count = 0
        while self.controller.is_open():
            self.update_count += 1
            if self.PQ.packet_ready():
                packet = self.PQ.generate_message()

                try:
                    self.controller.send_synchronous(packet)
                except serial.SerialException:
                    pass
            else:
                time.sleep(self.PQ.refresh_time)
                self.update_count = 0
                self.reset_count += 1
                print(self.reset_count)
                if self.reset_count > self.timeout:
                    self.controller.disconnect()
                    return



