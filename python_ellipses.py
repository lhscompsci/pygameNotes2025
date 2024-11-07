
import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((640,480))

white = (255,255,255)
screen.fill(white)

green = (0, 255, 0)
red = (255, 0 , 0)
r1 = (50, 10, 50, 100)
r2 = (90, 20, 100, 200)

pygame.draw.ellipse(screen, green, r1, 2)
pygame.draw.ellipse(screen, red, r2, 5)

# update the screen
pygame.display.update()

while (True):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
              pygame.quit(); 
              sys.exit();
            

