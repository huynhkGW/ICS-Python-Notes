#-----------------------------------------------------------------------------
# Name:        Actor movement example (key press and hold)
# Purpose:     And Example file demoing actors
#
# Author:      Mr. Brooks
# Created:     27-Oct-2020
# Updated:     27-Oct-2020
#-----------------------------------------------------------------------------
WIDTH = 200
HEIGHT = 200

gameState = ''

#Create the actor object
knight = Actor('knight_m_run_anim_f0')
#Give the actor a place on the screen to be
knight.pos = (100, 100)
#Make a move variable in the knight actor for our use
knight.move = False

def updateKnight():
    global knight  #I am changing the knight actor so i need it to be a global
    
    knight.x += 2; #Change the x position by a small amount to move it.
    

def on_key_down(key):
    '''Check to see if a key has been released'''
    global knight #I am changing the knight actor so i need it to be a global
    
    knight.move = True #Turn ON Key Movement


def on_key_up(key):
    '''Check to see if a key has been released'''
    global knight #I am changing the knight actor so i need it to be a global
    
    knight.move = False  #Turn OFF Key Movement
    

def update():
    '''This built in method is called once per frame'''
    #Notice I have NOT declared the knight as a global since I am NOT changing the variable
    if knight.move == True:  #Check if we should be moving the knight
        updateKnight()       #Move the knight

def draw():
    '''Draw loop for all the graphical elements to display'''
    #Empty the screen for each animation frame
    screen.fill((255, 255, 255))
    #Draw the knight
    knight.draw()