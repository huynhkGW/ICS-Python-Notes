#-----------------------------------------------------------------------------
# Name:        Dictionaries (dictionaries_ex1.py)
# Purpose:     This program detects a microbit and reads information from any active serial connections
#              Adapted From - https://stackoverflow.com/questions/58043143/how-to-set-up-serial-communication-with-microbit-using-pyserial
#
# Author:      Mr. Brooks-Prenger
# Created:     10-March-2021
# Updated:     13-March-2021
#-----------------------------------------------------------------------------
# Add your Python code here. E.g.
# from microbit import *
# import utime
# 
# while True:
#     
#     display.show(Image.HEART)
#     print('heart ', utime.ticks_ms())
#     utime.sleep_ms(100)
# 
# 
# 
# 
# #
import serial
import serial.tools.list_ports as list_ports
import time


def findMicrobitComPort(pid=516, vid=3368, baud=115200):
    '''
    This function finds a device connected to usb by it's PID and VID and returns a serial connection

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
    
    #Create the serial object
    serPort = serial.Serial(timeout=TIMEOUT)
    serPort.baudrate = baud
    
    #Search for device on open ports and return connection if found
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
    
    #If nothing found then return None
    return None




def main():
    print('looking for microbit')
    microbit = findMicrobitComPort()
    if not microbit:
        print('microbit not found')
        return
    
    print('opening and monitoring microbit port')
    microbit.open()
    
    dataCache = ''

    while True:
#         #Method 1
#         #Blocking version of serial read
#         #Slows down your entire program as it waits until there is a full line to be read before going
#         line = microbit.readline().decode('utf-8')
#         if line:  # If it isn't a blank line
#             print(line)


#         #Method 2 - Still slightly blocking, but better.
#         #WARNING - You need to have at least a 200ms delay in your microbit code or this method gets buggy
#         if (microbit.inWaiting()>0):
#            
#             data = microbit.readlines()  #Read lines into a list, one line per list entry
#                   
#             for i in range(len(data)): #Convert each entry in list from binary to a readable text format
#                 data[i] = data[i].decode('utf-8').strip()
#         
#         
#             print(data[-1])


#         #Method 3
#         #Proper Non-blocking version of serial read
#         #This method breaks up your code into tiny chunks/partial messages quite often.
#         #But it works with much shorter message durations.
#         if (microbit.inWaiting()>0):
#             #Method 2
#             data = microbit.read(microbit.inWaiting()).decode('utf-8') #read the bytes and convert from binary array to utf-8
#             print(data)
            

        #Method 4
        #Proper Non-blocking version of serial read with a cache to stop partial messages
        #If multiple lines of data are received between cycles only the most recent data is kept
        #It works with any message duration, but it's still recommended to have at least a 1ms delay in the microbit code
        if (microbit.inWaiting()>0):
            dataCache += microbit.read(microbit.inWaiting()).decode('utf-8')#.decode('utf-8') #read the bytes and convert from binary array to utf-8
            
            isFullLine = dataCache.count('\r\n')

            if isFullLine > 1:
                data = dataCache.rpartition('\r\n')#.strip() #split the data into 3 parts [useful, /r/n, cut off data]
                dataCache = data[-1]                         #Take the cut off data and save it for later
                data = data[0].rpartition('\r\n')[-1]        #Split the last complete chunk of data off and save (keeps only newest data sent by microbit)
                
                print(data)

    
    microbit.close()
    
main()