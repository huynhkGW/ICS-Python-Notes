
import pygame
 
pygame.init()
mainSurface = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 26)
 
 
def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text
 
 
loop = 1
while loop:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = 0
			
			
	mainSurface.fill((0, 0, 0))  #Wipe the screen
	
	mainSurface.blit(update_fps(), (10,0))  #Draw the returned rendered text on the surface
	print(clock.tick(60))  #Note - clock.tick returns the number of seconds since it was last called!
	
	pygame.display.flip()
 
pygame.quit()