import pygame
import random
    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    gameState = "start" #Set the gamestate to start on
    
    counter = 0 #A counter for demo purposes
    
    while True:
        print(f"Game Ticks: {pygame.time.get_ticks()} - gameState: {gameState}   counter: {counter}")
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Always need to do this, so needs to be outside the gamestate if statments!
            break                   #   ... leave game loop

        if gameState == "start":
            #Check for events needed in this case
            if ev.type == pygame.MOUSEBUTTONUP:
                gameState = "initialize"
            
            #Do what you want for the start screen
            mainSurface.fill((0, 200, 255))
        
        elif gameState == "initialize": #Sometimes it's useful to separate out initialization code into a gamestate
            #That will only run once when called and then change the state to something else.
            counter = 0
            gameState = "game"
            
        elif gameState == "game":
            mainSurface.fill((255, 200, 255))
            
            counter += 1
            if counter > 500:
                gameState = "start"
            
        
        else:
            print(f"Error - The program tried to load gamestate: {gameState}.  Resetting back to start")
            gameState = "start"

        

        


        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
