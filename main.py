from ZigBeeRx.RxController import *
from ZigBeeRx.xbeepacket import XBeePacket
from ZigBeeRx.GUI import PortSelectGUI
import argparse
import sys



def init_controller():

    txcont = RxController()                         # '/dev/tty.usbserial-AD01SSNN'
    txcont.connect()
    txcont.configure_remote()
    return txcont

def parse_arguments():
    parser = argparse.ArgumentParser(description="Initialization for the Receiving ZigBee")
    parser.add_argument('--port', type=str,
                        help="ZigBee serial port")
    parser.add_argument('--outfile', type=str,
                        help='Output KML file name (without ".kml"')
    args = parser.parse_args()
    if args.port:
        port = args.port
    if args.outfile:
        outfile = args.outfile

    if (args.port is None) and (args.outfile is None):
        with open('config.ini', 'r') as configfile:
            config = configfile.readlines()
            if len(config) != 2:
                print("Configuration file is not formatted properly or does not exist")
                sys.exit(-1)
            else:
                port = config[0]
                outfile = config[1]
    elif args.port is None:
        with open('config.ini', 'r') as configfile:
            config = configfile.readlines()
            if len(config) != 2:
                print("Configuration file is not formatted properly or does not exist")
                sys.exit(-1)
            else:
                port = config[0]
    elif args.outfile is None:
        with open('config.ini', 'r') as configfile:
            config = configfile.readlines()
            if len(config) != 2:
                print("Configuration file is not formatted properly or does not exist")
                sys.exit(-1)
            else:
                port = config[1]
    elif args.port or args.outfile:
        with open('config.ini', 'w') as configfile:
                configfile.write(args.port)
                configfile.write("\n")
                configfile.write(args.outfile)


    return port, outfile




def main(argv):
    args = parse_arguments()
    rx = init_controller()
    while True:
        try:
            rx.receive_from()
        except KeyboardInterrupt:
            break



main()
