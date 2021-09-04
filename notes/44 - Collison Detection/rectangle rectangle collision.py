import pygame
import random
import math

    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    # Create the the size, position and color for a rectangle
    rectangleDimensions  = [200,200,100,30] #[left, top, width, height] aka #[x, y-, width, height]
    
    rectangleColor = (255,0,0)
    
    # Create the the size, position and color for another rectangle that follows the mouse
    mouseX, mouseY = pygame.mouse.get_pos()  #Get the position tuple and save it into two variables
    mouseRectangleDimensions = [mouseX,mouseY,100,50]
    mouseRectangleColor = (0,0,255)
    
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...
        #Have the mouse Rectangle always follow the mouse
        mouseX, mouseY = pygame.mouse.get_pos()
        mouseRectangleDimensions[0] = mouseX
        mouseRectangleDimensions[1] = mouseY
        mouseRectWidth = mouseRectangleDimensions[2]
        mouseRectHeight = mouseRectangleDimensions[3]
        
        #Separate the rect into more understandable variables (not necessary, done to make algorithm clearer)
        rectX = rectangleDimensions[0]
        rectY = rectangleDimensions[1]
        rectWidth  = rectangleDimensions[2]
        rectHeight = rectangleDimensions[3]
        
        if (mouseX + mouseRectWidth > rectX and mouseX < rectX + rectWidth and mouseY + mouseRectHeight > rectY and mouseY < rectY + rectHeight):
            #A collision happens!
            rectangleColor = (100,0,0)
        else:
            #no collision happened
            rectangleColor = (255,0,0)
  
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        pygame.draw.rect(mainSurface, rectangleColor, rectangleDimensions) #Draw Rectangle
        pygame.draw.rect(mainSurface, mouseRectangleColor, mouseRectangleDimensions) #Draw mouseRectangle
        

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
