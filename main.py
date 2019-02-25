from ZigBeeRx.RxController import *
from ZigBeeRx.xbeepacket import XBeePacket
from ZigBeeRx.GUI import PortSelectGUI
#from ZigBeeRx.threads import RxThread


def init_controller():
    # port_select = PortSelectGUI()
    # port_select.display()
    port = port_select.port
    txcont = RxController(port)                         # '/dev/tty.usbserial-AD01SSNN'
    txcont.connect()
    txcont.configure_remote()
    return txcont





def main():
    rx = init_controller()
    while True:
        try:
            rx.receive_from()
        except KeyboardInterrupt:
            break



main()
