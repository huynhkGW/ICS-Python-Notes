#-----------------------------------------------------------------------------
# Name:        actors - lists of actors
# Purpose:     An example file demoing lists actors
#
# Author:      Mr. Brooks
# Created:     28-Oct-2020
# Updated:     28-Oct-2020
#-----------------------------------------------------------------------------
import random

WIDTH = 200
HEIGHT = 200


#Create the actor object
knight = Actor('knight_m_run_anim_f0',  (random.randint(0,WIDTH),random.randint(0,HEIGHT)))

ships = []               #Create a blank list
for i in range(10):      #Loop 10 times, and add 10 actors to the list
    ships.append( Actor('ship',  (random.randint(0,WIDTH),random.randint(0,HEIGHT))))

def on_mouse_down():
    global ships
    #Reposition the ships on a click
    for ship in ships:
        ship.pos = (random.randint(0,WIDTH),random.randint(0,HEIGHT))
        

def draw():
    '''Draw loop for all the graphical elements to display'''
    #Empty the screen for each animation frame
    screen.fill((255, 255, 255))
    
    #Draw the knight
    knight.draw()
    
    #Draw all the ships
    for ship in ships:
        ship.draw()