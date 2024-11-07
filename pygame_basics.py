
# all imports go at the top
import pygame, sys


# create the screen
pygame.init()
screen = pygame.display.set_mode((800,600))


# Colors the screen white
white = (255, 255, 255 )
screen.fill( white )

# Updates the display
pygame.display.update()
           
while( True ):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
              pygame.quit(); 
              sys.exit();
            
