#-----------------------------------------------------------------------------
# Name:        actors with images example
# Purpose:     And Example file demoing actors
#
# Author:      Mr. Brooks
# Created:     01-Oct-2020
# Updated:     01-Oct-2020
#-----------------------------------------------------------------------------
WIDTH = 200
HEIGHT = 200

gameState = ''

#Create the actor object
knight = Actor('knight_m_run_anim_f0')
#Give the actor a place on the screen to be
knight.pos = (100, 100)
#Set the starting image number
knight.frame = 0

def updateKnight():
    global knight
    knight.frame = knight.frame + 1
    
    #What do these lines fix?
    if knight.frame > 3:
        knight.frame = 0
        
    #Assign a new image name based on the updated frame number
    knight.image = 'knight_m_run_anim_f' + str(knight.frame)
    

def on_key_up(key):
    '''Check to see if a key has been released'''
    global gameState #Make sure you make globals if necessary
    global knight
    
    if key == keys.A:
        #Schedule the animation to run instead of calling it just once!
        #updateKnight()
        clock.schedule_interval(updateKnight, 0.1)
    
    if key == keys.Z:
        #Stop the animation
        clock.unschedule(updateKnight)
    


def draw():
    '''Draw loop for all the graphical elements to display'''
    #Empty the screen for each animation frame
    screen.fill((255, 255, 255))
    #Draw the knight
    knight.draw()