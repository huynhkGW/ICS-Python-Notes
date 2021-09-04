#This program detects a microbit and reads information from any active serial connections
#Adapted From - https://stackoverflow.com/questions/58043143/how-to-set-up-serial-communication-with-microbit-using-pyserial

import serial
import serial.tools.list_ports as list_ports

#Required information about the microbit so it can be found
PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1


def findComPort(pid, vid, baud):
    '''
  This function finds a device connected to usb by it's PID and VID and returns a serial connection
  
  Parameters
  ----------
  None

  Returns
  -------
  float
    The value of the Seidelonian constant.
  '''
    ''' return a serial port '''
    serPort = serial.Serial(timeout=TIMEOUT)
    serPort.baudrate = baud
    ports = list(list_ports.comports())
    print('scanning ports')
    for p in ports:
        print('port: {}'.format(p))
        try:
            print('pid: {} vid: {}'.format(p.pid, p.vid))
        except AttributeError:
            continue
        if (p.pid == pid) and (p.vid == vid):
            print('found target device pid: {} vid: {} port: {}'.format(
                p.pid, p.vid, p.device))
            serPort.port = str(p.device)
            return serPort
    return None




def main():
    print('looking for microbit')
    microbit = findComPort(PID_MICROBIT, VID_MICROBIT, 115200)
    if not microbit:
        print('microbit not found')
        return
    print('opening and monitoring microbit port')
    microbit.open()
    
    while True:
        line = microbit.readline().decode('utf-8')
        if line:  # If it isn't a blank line
            print(line)
    
    microbit.close()
    
main()