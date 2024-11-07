
import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((640,480))

white = (255,255,255)
screen.fill(white)

# make a few colors
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 128, 0)

pygame.draw.rect(screen, green, (10,10,50,50),4)
pygame.draw.rect(screen, red, (50,100,80,60), 7)
pygame.draw.rect(screen, blue, (350,300,100,50), 5)
pygame.draw.rect(screen, black, (250,200,50,100), 4)

pygame.draw.rect(screen, blue, (150,300,100,50))
pygame.draw.rect(screen, black, (450,200,50,100))

# update the screen
pygame.display.update()

while (True):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
              pygame.quit(); 
              sys.exit();
            

