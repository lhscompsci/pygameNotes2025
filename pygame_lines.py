#(c) A+ Computer Science
#www.apluscompsci.com

import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((640,480))


white = (255,255,255)
screen.fill(white)

green = (0, 255, 0)
red = (255, 0 , 0)

point1 = ( 50, 50 )
point2 = ( 150, 150 )

pygame.draw.line(screen, green, point1, point2)

point1 = ( 50, 100 )
point2 = ( 50, 150 )
pygame.draw.line(screen, red, point1, point2)


# update the screen
pygame.display.update()

while (True):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
              pygame.quit(); 
              sys.exit();
            
                          

