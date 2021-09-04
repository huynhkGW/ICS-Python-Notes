#-----------------------------------------------------------------------------
# Name:        Using microbit class (using microbit class.py)
# Purpose:     This program is an example to demonstrate how to use the Microbit class.
#
# Author:      Mr. Brooks-Prenger
# Created:     10-March-2021
# Updated:     7-April-2021
#-----------------------------------------------------------------------------
#--------------------------EXAMPLE CODE TO RUN ON MICROBIT -------------------
# from microbit import *
# import utime
# 
# while True:
#     
#     display.show(Image.HEART)
#     print('heart ', utime.ticks_ms())
#     utime.sleep_ms(15)
# 
#-----------------------------------------------------------------------------
# 
from Microbit import *


def loadSingleMicrobit():
    '''Load a single microbit connection'''
    #Create microbit instance
    mb = Microbit()
    
    #Check to make sure it's working
    if not mb.isReady():
        print('Error, Problem Loading Microbit.  Exiting Program')
        return
         
    #return mb#TEMP FOR DEBUGGING
    while True:
        
        line = mb.nonBlockingReadRecentLine()
        if line != None:
            print(line)
        
    mb.closeConnection()


def loadMicrobits():
    '''Load all microbits connected to computer and save them to a list'''
    
    #Search for and load up ALL microbits connected to computer
    mbList = []  #List to store all microbits
    while True:    
        mbPortList = []
        for mb in mbList:
            mbPortList.append(mb.getPort())

        
        #Create microbit instance
        #print(f"create a microbit instance with exclusions : {mbPortList}")
        mb = Microbit(mbPortList)
         
        #Check if this is a valid ready to use microbit instance
        if not mb.isReady():
            print(f'{len(mbList)} microbits loaded on {mbPortList}. Continuing to next stage.')
            break
        
        mbList.append(mb)
        
    if len(mbList) < 1:
        print('Error, no microbits found.  Ending Script')
        return
    
    
    #Read information sent by every microbit
    while True:
    
        for mb in mbList:
            line = mb.nonBlockingReadRecentLine()
            if line != None:
                print(line)
                
            
        
    #Close all microbit connections when done reading
    for mb in mbList:
        mb.closeConnection()
    

loadMicrobits()