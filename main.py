from ZigBeeRx.RxController import *
import time
import argparse
import ZigBeeRx.KML_Formater as KML

name = 'data.kml'
port = 'COM10' #sets default port

def init_controller():
    txcont = RxController(port)
    txcont.connect()
    txcont.configure_remote()
    return txcont


def main():
    print('This script will receive data from an Xbee and write it to a KML file')
    global port
    port = input("Enter com port (ex 'COM7') : ")
    KML.kml_name(str(input('Enter a name for the .kml file to make or add to : ')))
    rx = init_controller()
    print("Please wait two seconds before starting transmit.\n")
    time.sleep(2)
    print('Start the transmitter now.\n')

    while True:
        try:
            rx.receive_from()
        except KeyboardInterrupt:
            print('Program Ended with Ctrl-C.\n')
            break
    return 0

if __name__ == '__main__':
    main()