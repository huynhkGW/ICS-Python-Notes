import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    # Set up some data to describe a small circle and its color
    circlePos = [50,100]  #X and Y Values
    circleSize = 30  
    circleColor = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)
    
    circlePos2 = [50,300]  #X and Y Values
    circleSize2 = 30  
    circleColor2 = (0, 0, 255)        # A color is a mix of (Red, Green, Blue)

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        
        #Move the circle
        #circlePos[0] = circlePos[0] +1
        circlePos[0] += 1
        circlePos2[0] += 1
        
        # Draw a circle on the surface
        pygame.draw.circle(mainSurface, circleColor, circlePos, circleSize)
        pygame.draw.circle(mainSurface, circleColor2, circlePos2, circleSize2)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()