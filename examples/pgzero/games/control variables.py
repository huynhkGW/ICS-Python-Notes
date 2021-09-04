#-----------------------------------------------------------------------------
# Name:        Control variables Examples 
# Purpose:     Example to show how to use a control variable
#
# Author:      Mr. Brooks
# Created:     01-Oct-2020
# Updated:     01-Oct-2020
#-----------------------------------------------------------------------------


brushLocation = (400,300)
drawEnabled = False

def on_mouse_move(pos, rel, buttons):
    global brushLocation
    global drawEnabled
    
    #Save the brush location (x and y) as it updates
    brushLocation = pos
    
    #Check for the left button to be pressed down
    if mouse.LEFT in buttons:
        print("Yay! The button was clicked")
        drawEnabled = True
    else:
        drawEnabled = False


def draw():
    global brushLocation
    global drawEnabled
    #screen.clear()
    if drawEnabled == True:
        screen.draw.circle(brushLocation, 3, 'white')

