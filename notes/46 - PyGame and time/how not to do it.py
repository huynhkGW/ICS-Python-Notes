import pygame
import random

class Ball():
    
    def __init__(self, posIn, sizeIn, colorIn):
        self.pos = posIn
        self.size = sizeIn
        self.color = colorIn 
        
    def draw(self, surfaceIn):
        pygame.draw.circle(surfaceIn, self.color, self.pos, self.size)
        
    def move(self, xIn=0, yIn=0):
        self.pos[0] += xIn
        self.pos[1] += yIn
        
#         #Another way to do it
#         self.pos = ( self.pos[0] + xIn, self.pos[1].yIn)
        pass
    
    def setPos(self, xIn=0, yIn=0):
        #TODO Set the position of the ball to xIn and yIn
        pass
        
    def distFromPoint(self, xIn, yIn):
        #https://www.khanacademy.org/math/geometry/hs-geo-analytic-geometry/hs-geo-distance-and-midpoints/v/distance-formula#:~:text=Learn%20how%20to%20find%20the,distance%20between%20any%20two%20points.
        #TODO: Given an x and y input return the distance the ball is from this point
        pass
    
    def collidePoint(self, xIn, yIn):
        #Challenge!
        #TODO check to see if the point is inside the circle.  If so return true, otherwise false.
        pass
    
    def collideXXXX(self):
        #Even more challenge
        #TODO Add another collison check for a differnt object type (another Ball, a rect, etc.)
        pass

 #   def bounce(self):
   
class Character():
    
    def __init__(self, imgIn, posIn):
        self.image = imgIn
        self.pos = posIn

    def update(self):
        return

    def draw(self, target_surface):
        return

    def handle_click(self):
        return

    def contains_point(self, pt):
        # Use code from QueenSprite here
        return
    
    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    # Create the ball object using it's position, size and color
    circle = Ball([50,100], 30, (255, 0, 0))        # A color is a mix of (Red, Green, Blue)
    
    circles = []
    for i in range(5): #Add 5 balls to the list of circles
        circles.append(Ball([random.randrange(surfaceSize),random.randrange(surfaceSize)], 30, (0, 0, 0)) )

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...
        pygame.time.wait(1000)
        circles.append(Ball([random.randrange(surfaceSize),random.randrange(surfaceSize)], 30, (0, 0, 0)) )

        
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        
        #Move the circle
        #circle.pos[0] += 1  #TODO: Replace with with the move() method.
        circle.move(1,0)
        # Draw the circle on the surface
        circle.draw(mainSurface)
        
        for i in range(len(circles)):
            circles[i].move(1,0)
            circles[i].draw(mainSurface)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
