#-----------------------------------------------------------------------------
# Name:        Dictionaries (dictionaries_ex1.py)
# Purpose:     This program detects reads the microbit data and displays the gyro results
#
# Author:      Mr. Brooks-Prenger
# Created:     10-March-2021
# Updated:     13-March-2021
#-----------------------------------------------------------------------------
'''Code to be run on the microbit:
from microbit import *
import speech

DELAY_VALUE =100

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    print("x, y, z:", x, y, z)
    #display.show(Image.YES)
    sleep(DELAY_VALUE)
    #display.show(Image.NO)
    #sleep(DELAY_VALUE)
 '''
#-----------------------------------------------------------------------------


import pygame
import serial
import serial.tools.list_ports as list_ports

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

def normalizeGyroValue(gyroString, startingY, displayRect):
    '''
    This function normalizes the gyro values from ~ +/- 1050 to  ~ +/- 200 to fit on screen

    Parameters
    ----------
    gyroString - The gyro value as a string
    startingY - The initial y value to place the rect at
    displayRect - The rect value to be modified to create the bar

    Returns
    -------
    None - Values required are changed in displayRec as passed by value

    '''
    
    gyroValue = int(gyroString)
    
    gyroValue = (gyroValue/1050)*200 #Reduce gyrovalue to only scale between approx -200 and 200

    if gyroValue < 0:
        displayRect[1] = startingY+gyroValue
        displayRect[3] = -gyroValue
    else:
        displayRect[1] = startingY
        displayRect[3] = gyroValue
        
    #No need to return anything as I am using the fact that the Rect passed in is a list
    #So any changes made will propograte back to the main function without a return statement (pass by ref)




def main():
    
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower


    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    programState = "initialize"
    

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        if programState == "initialize":
            #TODO set up the intial data for my 3 bar graphs
            #TODO Draw a loading message
            startingY =240
            gyroXRectBase = [50,startingY,25,50]
            gyroYRectBase = [100,startingY,25,0]
            gyroZRectBase = [150,startingY,25,0]
            
            
            programState = "set up microbit"
            
        elif programState == "set up microbit":
            print('looking for microbit')
            microbit = findMicrobitComPort()
            if not microbit:
                print('microbit not found')
                continue
            
            print('opening and monitoring microbit port')
            microbit.open()
            
            programState = "display"
            
        elif programState == "display":
            #Grab the data from the microbit
            line = microbit.readline().decode('utf-8')
            #print(line)
            if line:  # If it isn't a blank line
                #Update your data
                #print(line)
                data = line.split()
                #print(data)
                var1, var2 = [1,2]
                *label, gyroX, gyroY, gyroZ = data
                print(f' ({gyroX}, {gyroY}, {gyroZ})')

                normalizeGyroValue(gyroX, startingY, gyroXRectBase)
                normalizeGyroValue(gyroY, startingY, gyroYRectBase)
                normalizeGyroValue(gyroZ, startingY, gyroZRectBase)
                
                #print(gyroXRectBase)
                
            mainSurface.fill((0, 200, 255))
            
            #Draw the bars on the screen
            pygame.draw.rect(mainSurface, (255,0,0), gyroXRectBase)
            pygame.draw.rect(mainSurface, (0,255,0), gyroYRectBase)
            pygame.draw.rect(mainSurface, (0,0,255), gyroZRectBase)
            


        pygame.display.flip() #Update the display
        clock.tick(60) #Force frame rate to be slower

    #-----------------END of main while True loop!------------------------------
    if microbit != None:
        microbit.close()  #Close the microbit serial connection
    pygame.quit()     # Once we leave the loop, close the window.
    

main()