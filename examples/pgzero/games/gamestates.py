#-----------------------------------------------------------------------------
# Name:        gamestate Examples (newFile.py)
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     01-Oct-2020
# Updated:     01-Oct-2020
#-----------------------------------------------------------------------------

gameState = ''

def startUp():
    '''Run this to get the program ready to run'''
    global gameState

    gameState = 'start screen'
    

def on_key_up(key):
    '''Check to see if a key has been released'''
    global gameState #Make sure you make globals if necessary
    
    if key == keys.A:
        gameState = 'win'


def draw():
    '''Draw loop for all the graphical elements to display'''
    if gameState == "start screen":
        screen.clear()
        screen.fill((255, 255, 255))
        screen.draw.text("Hello, Welcome to my program", (25, 30), color="orange")
        screen.draw.text("Press the secret key", (25, 70), color="red")
        
    elif gameState == "win":
        screen.clear()
        screen.fill((255, 255, 255))
        screen.draw.text("You win!", (25, 30), color="orange")
    else:
        screen.clear()
        screen.fill((255, 255, 255))
        screen.draw.text("Error, no game state loaded", (25, 30), color="orange")


startUp()