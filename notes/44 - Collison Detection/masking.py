import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 1000   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    vitaImage = pygame.image.load("images/DinoSprites - vita - single frame.png")
    vitaImage.set_colorkey((255,255,255))
    vitaImage.convert_alpha()
    vitaPos = pygame.mouse.get_pos()
    vitaMask = pygame.mask.from_surface(vitaImage)

    mazeImage = pygame.image.load("images/Maze.png")
    mazeImage.convert_alpha()
    mazeMask = pygame.mask.from_surface(mazeImage)
    mazePos = (150,150)
 

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...
        vitaPos = pygame.mouse.get_pos()
        offset = ( vitaPos[0] - mazePos[0],vitaPos[1] - mazePos[1])
        print(mazeMask.overlap(vitaMask, offset))
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))
        mainSurface.blit(vitaImage, vitaPos)
        mainSurface.blit(mazeImage, mazePos)
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()