#-----------------------------------------------------------------------------
# Name:        Button Examples 
# Purpose:     Example to show how to use a Rect to make a button
#
# Author:      Mr. Brooks
# Created:     03-Oct-2020
# Updated:     06-Oct-2020
#-----------------------------------------------------------------------------


#Define size of the window
WIDTH = 300
HEIGHT = 300


#Create the first button
button1Draw = [0, 0, 100, 20] #[left, top, width, height]
button1Rect = Rect(button1Draw) #create a rect https://www.pygame.org/docs/ref/rect.html
button1Value = False  #Give the button a value
button1Color = 'blue' #Give the buttton a color, can also use (r, g, b) sets
button1Rect.center = (150, 150) #Set the location of the button, discuss rect location values



def on_mouse_up(pos, button): #https://pygame-zero.readthedocs.io/en/stable/hooks.html
    '''Pygame Special Event Hook - Runs when the mouse button is released'''

    global button1Color
    global button1Value
    
    #Check to see if button1 is clicked     
    if button1Rect.collidepoint(pos):  #https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidepoint
        print("Button 1 Clicked!", button1Value)
        
        #Swap colors (no control variable)
        if button1Color == 'blue':
            button1Color = 'white'
        else:
            button1Color = 'blue'


        #Swap color using a control Variable - Making the button more useful
#         if button1Value == True:
#             button1Color = 'white'
#             button1Value = False
#         else:
#             button1Color = 'blue'
#             button1Value = True

  

def draw():
    pass
    #Draw the button on the screen
    screen.draw.filled_rect(button1Rect, button1Color) #filled_rect(rect, (r, g, b)) #could just use rect
    screen.draw.text("Wow!", (120,145))
    