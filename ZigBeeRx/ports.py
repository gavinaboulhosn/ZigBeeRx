import sys
import glob
import serial


def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM{}'.format((i+1) for i in range(256))]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported OS')

    result = []
    if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        for port in ports:
            result.append(port)
        return result
    else:
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

