#-----------------------------------------------------------------------------
# Name:        actors with images example
# Purpose:     And Example file demoing actors
#
# Author:      Mr. Brooks
# Created:     01-Oct-2020
# Updated:     01-Oct-2020
#-----------------------------------------------------------------------------
import pygame  #Need this as we are going to use some core pygame functoinality instead of just PyGame Zero

#Set the size of the game window
WIDTH = 200
HEIGHT = 200


#Create the actor object
knight = Actor('knight_m_run_anim_f0')
#Give the actor a place on the screen to be
knight.center = (100, 100)


def on_key_down(key, mod, unicode):
    '''Check to see if a key has been released'''
    global knight
    
    if key == keys.A:
        knight = inflate(knight, 50,25)


def draw():
    '''Draw loop for all the graphical elements to display'''
    #Empty the screen for each animation frame
    screen.fill((255, 255, 255))
    #Draw the knight
    knight.draw()
    

def inflate(actorIn, xIncrease, yIncrease):
        '''Increase the size of an actor by the given amount
        
        Parameters
        ----------
        actorIn - The actor to work with
        xIncrease - The amount (in pixels) to increase the width by, use a negative number to shrink
        yIncrease - The amount (in pixels) to increase the height by, use a negative number to shrink
        
        Returns
        -------
        The modified actor object
        '''
        #Scale the size of the knight to 100x100 if the A key is pressed
        oldLocation = knight.center #Save the current centre point of the actor
        currentXSize = knight.width
        currentYSize = knight.height
        actorIn._surf = pygame.transform.scale(actorIn._surf, (currentXSize + xIncrease, currentYSize + yIncrease)) #Scale the actor to a new height and width
        actorIn._update_pos() #Update the position of the actor to account for the scaling
        actorIn.center = oldLocation #Set the actor's location back to it's starting point
        return actorIn