import pygame
import random
import math

class Ball():
    
    def __init__(self, posIn, sizeIn, colorIn):
        self.pos = posIn
        self.size = sizeIn
        self.color = colorIn
        self.xDirection = 0
        self.yDirection = 0
        self.speed = 1
        
        
    def draw(self, surfaceIn):
        pygame.draw.circle(surfaceIn, self.color, self.pos, self.size)
        
    def move(self):
        self.pos[0] += self.speed * self.xDirection
        self.pos[1] += self.speed * self.yDirection
        
    def update(self):
        self.move()
        
    def setSpeed(self, speedIn=0):
        self.speed = speedIn
    
    def setDirection(self, angleDegIn):  #angle in is in degrees
        #Convert degrees to rad
        angleRad = math.radians(angleDegIn)
        self.xDirection = math.cos(angleRad)
        self.yDirection = -math.sin(angleRad)
        
    def setDirectionToPoint(self, pointIn): #Expecting Tuple with x and y
        #Find the angle to the point
        deltaX = pointIn[0] - self.pos[0]
        deltaY = self.pos[1] - pointIn[1]
        thetaRad = math.atan2(deltaY,deltaX)
        thetaDeg = math.degrees(thetaRad)
        #set the direction
        print(thetaDeg)
        self.setDirection(thetaDeg)

    def setPos(self, xIn=0, yIn=0):
        #TODO Set the position of the ball to xIn and yIn
        pass
        
    def distFromPoint(self, xIn, yIn):
        #https://www.khanacademy.org/math/geometry/hs-geo-analytic-geometry/hs-geo-distance-and-midpoints/v/distance-formula#:~:text=Learn%20how%20to%20find%20the,distance%20between%20any%20two%20points.
        #TODO: Given an x and y input return the distance the ball is from this point
        pass

    
    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    # Create the ball object using it's position, size and color
    redBall = Ball([50,100], 30, (255, 0, 0))        # A color is a mix of (Red, Green, Blue)
    redBall.setSpeed(1)
    redBall.setDirection(0)
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.MOUSEBUTTONUP:
            redBall.setDirectionToPoint(ev.pos)
            pass

        # Update your game objects and data structures here...


        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        #Move the circle
        redBall.update()
        # Draw the circle on the surface
        redBall.draw(mainSurface)
        
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
