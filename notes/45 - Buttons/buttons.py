import pygame
import random

class Button():
    
    def __init__(self, rectIn, colorIn, valueIn=False ):
        self.rect = rectIn
        self.displayColor = colorIn
        self.baseColor = colorIn
        self.hoverColor = pygame.Color(0,0,0)
        if self.baseColor.r > 50: self.hoverColor.r = self.baseColor.r - 50
        if self.baseColor.g > 50: self.hoverColor.g = self.baseColor.g - 50
        if self.baseColor.b > 50: self.hoverColor.b = self.baseColor.b - 50
        
        
        self.value = valueIn
        
        
        
    def draw(self, surfaceIn):
        pygame.draw.rect(surfaceIn, self.displayColor, self.rect, border_radius =20)
        
    def update(self):
        if self.collidePoint(pygame.mouse.get_pos()):
          
            self.displayColor = self.hoverColor
        else:
            self.displayColor = self.baseColor
            
        
        
      
    def setPos(self, xIn=0, yIn=0):
        #TODO Set the position of the ball to xIn and yIn
        pass

    def collidePoint(self, pointIn):
        #Not necessary, but to make the algorithm easier for ya'll to see
        rectX = self.rect[0]
        rectY = self.rect[1]
        rectWidth = self.rect[2]
        rectHeight = self.rect[3]
        
        xIn = pointIn[0]
        yIn = pointIn[1]
        
        if (xIn > rectX and xIn < rectX + rectWidth and yIn > rectY and yIn < rectY + rectHeight):
            return True
        else:
            return False
        
    def toggleValue(self):
        self.value = not self.value
        print(f"The button is now {self.value}")
        
    def getValue(self):
        return self.value
        
    
 
    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    # Create the ball object using it's position, size and color
    greenButton = Button( [50,50,100,25], pygame.Color(0,255,0))
    redButton = Button( [50,100,100,25], pygame.Color(255,0,0))
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.MOUSEBUTTONUP:
            if greenButton.collidePoint(pygame.mouse.get_pos()):
                greenButton.toggleValue()

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        greenButton.update()
        greenButton.draw(mainSurface)
        redButton.update()
        redButton.draw(mainSurface)
        
        if greenButton.getValue():
            pygame.draw.circle(mainSurface, (255,0,0), (200,200), 50)

        
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
