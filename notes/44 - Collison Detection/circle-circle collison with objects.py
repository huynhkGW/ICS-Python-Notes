import pygame
import random
import math

class Ball():
    
    def __init__(self, posIn, sizeIn, colorIn):
        self.pos = posIn
        self.size = sizeIn
        self.color = colorIn 
        
    def draw(self, surfaceIn):
        pygame.draw.circle(surfaceIn, self.color, self.pos, self.size)
    
    def update(self):
        pass
        
    def move(self, xIn=0, yIn=0):
        self.pos[0] += xIn
        self.pos[1] += yIn
        
    def setPos(self, posIn):
        self.pos = posIn


    def distFromPoint(self, point):
        #Distance from a point given by tuple (x,y)
        distance = math.sqrt( ((self.pos[0]-point[0])**2)+((self.pos[1]-point[1])**2) )
        
        return distance
    
    def collidePoint(self, point):
        if self.distFromPoint(point) < self.size:
            return True
        else:
            return False
        
    def collideCircle(self, circle):
        if self.distFromPoint(circle.pos) < (self.size + circle.size):
            return True
        else:
            return False        
    

    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    # Create the ball object using it's position, size and color
    circle = Ball([200,200], 30, (255, 0, 0))        # A color is a mix of (Red, Green, Blue)
    mouseCircle = Ball([50,100], 50, (0, 0, 255))       
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...
        
        mouseCircle.setPos(pygame.mouse.get_pos())
#         if mouseCircle.collidePoint(circle.pos):
#             print("hit")
#             circle.color=(100,0,0)
#         else:
#             circle.color=(255,0,0)
#         
        if mouseCircle.collideCircle(circle):
            #print("hit")
            circle.color=(100,0,0)
        else:
            circle.color=(255,0,0)
                
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        circle.draw(mainSurface)
        mouseCircle.draw(mainSurface)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
