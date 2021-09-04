#Define size of the window
WIDTH = 300
HEIGHT = 300
RECT = 0
VALUE = 1
COLOR = 2

#Create the first button
button1 = [ Rect([0, 0, 100, 20]), False, 'blue'] #[Rect, Value, Color]


def on_mouse_up(pos, button): #https://pygame-zero.readthedocs.io/en/stable/hooks.html
    '''Pygame Special Event Hook - Runs when the mouse button is released'''
    global button1
    #global button1Color
    
    #Check to see if button1 is clicked     
    if button1[RECT].collidepoint(pos):  #https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidepoint
        print("Button 1 Clicked!")
        
        #Swap color
        if button1[COLOR] == 'blue':
            button1[COLOR] = 'white'
        else:
            button1[COLOR] = 'blue'

  

def draw():

    #Draw the button on the screen
    screen.draw.filled_rect(button1[RECT], button1[COLOR]) #filled_rect(rect, (r, g, b)) #could just use rect    
