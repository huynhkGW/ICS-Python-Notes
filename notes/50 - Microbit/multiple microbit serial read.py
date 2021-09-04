#-----------------------------------------------------------------------------
# Name:        Dictionaries (dictionaries_ex1.py)
# Purpose:     This program detects a microbit and reads information from any active serial connections
#              Adapted From - https://stackoverflow.com/questions/58043143/how-to-set-up-serial-communication-with-microbit-using-pyserial
#
# Author:      Mr. Brooks-Prenger
# Created:     29-March-2021
# Updated:     29-March-2021
#-----------------------------------------------------------------------------

import serial
import serial.tools.list_ports as list_ports


def findMicrobitsComPort(pid=516, vid=3368, baud=115200):
    '''
    This function finds all microbits connected via usb and returns a list of serial connections

    Parameters
    ----------
    pid - Product id of device to search for
    vid - Vendor id of device to search for
    baud - Baud rate to open the serial connection at

    Returns
    -------
    Serial - If a device is found a serial connection for the device is configured and returned

    '''
    #Required information about the microbit so it can be found
    #PID_MICROBIT = 516
    #VID_MICROBIT = 3368
    TIMEOUT = 0.1
    
    
    
    
    #Search for device on open ports and return connection if found
    serPortList = []
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
            
            #Create the serial object and add to a list
            serPort = serial.Serial(timeout=TIMEOUT)
            serPort.baudrate = baud
            serPort.port = str(p.device)
            serPortList.append(serPort)
            #return serPort
    
    #If nothing found then return None
    if len(serPortList) == 0:
        return None
    else:
        return serPortList


def main():
    print('looking for microbit')
    microbit = findMicrobitsComPort()
    
    if not microbit:
        print('no microbits not found')
        return
    
    print(f'opening and monitoring {len(microbit)} microbit port(s)')
    for bit in microbit:
        bit.open()

    while True:
        
        for bit in microbit:
            line = bit.readline().decode('utf-8')
            if line:  # If it isn't a blank line
                print(line)
    
    for bit in microbit:
        bit.close()
    
main()