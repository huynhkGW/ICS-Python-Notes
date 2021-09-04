#-----------------------------------------------------------------------------
# Name:        actors with images example
# Purpose:     And Example file demoing actors
#
# Author:      Mr. Brooks
# Created:     02-Nov-2020
# Updated:     02-Nov-2020
#-----------------------------------------------------------------------------
import math
WIDTH = 200
HEIGHT = 200

#Create the actor object
knight = Actor('knight_m_run_anim_f0')
knight2 = Actor('knight_m_run_anim_f0',(50,50))
#Give the actor a place on the screen to be
knight.pos = (100, 100)

#The following are all custom attributes https://www.pygame.org/docs/ref/rect.html
knight.move = False   #Make a move variable in the knight actor for our use
knight.speed = 0.5    #Speed for the knight to move at
knight.xDirection = 1 #Amount to move in x Direction
knight.yDirection = 1 #Amount to move in y Direction



def on_mouse_up(pos):
    #Get the angle to the mouse pointer, and set that as the new angle for the knight.
    knight.angle = knight.angle_to(pos)
    print(f'angle: {knight.angle}')
    
    #The following is all based on the idea of the trig unit circle
    #https://www.mathsisfun.com/geometry/unit-circle.html
    knight.xDirection = math.cos(math.radians(knight.angle))
    knight.yDirection = -math.sin(math.radians(knight.angle))
    print(f'Directional components:({knight.xDirection},{knight.yDirection}')


def on_key_down(key):
    '''Check to see if a key has been released'''
    global knight
    
    #If the A key is pressed
    if key == keys.A:
        #Flip the value of knight.move (ie. True <--> False)
        knight.move = not knight.move
         
def on_key_up(key):
    pass

def update():
    global knight
    
    if knight2.colliderect(knight):
        print('ouch!', knight2.angle_to(knight))
        newAngle = knight2.angle_to(knight) +90
        knight.xDirection = math.cos(math.radians(newAngle))
        knight.yDirection = -math.sin(math.radians(newAngle))
        
    
    if knight.move:
#         knight.x += 1  #knight.speed
#         knight.y += 1  #knight.speed
        knight.x += knight.speed*knight.xDirection #Change the x position by a small amount to move it.
        knight.y += knight.speed*knight.yDirection


def draw():
    '''Draw loop for all the graphical elements to display'''
    #Empty the screen for each animation frame
    screen.fill((255, 255, 255))
    #Draw the knight
    knight.draw()
    knight2.draw()