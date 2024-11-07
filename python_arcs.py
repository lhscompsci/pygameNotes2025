
import pygame
import sys
from math import pi

pygame.init()

screen = pygame.display.set_mode((640,480))

white = (255,255,255)
screen.fill(white)

green = (0, 255, 0)
red = (255, 0 , 0)
r1 = ((10, 10), (100, 100))
r2 = ((20, 60), (200, 60))

pygame.draw.arc(screen, green, r1, 0, pi/2, 2)
pygame.draw.arc(screen, red, r2, 0, pi, 5)

# update the screen
pygame.display.update()

while (True):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
              pygame.quit(); 
              sys.exit();
            

