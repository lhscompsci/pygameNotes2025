import pygame
import random
import sys

from pygame.locals import *

# create the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))

# color in the screen white
white = (255, 255, 255)
screen.fill(white)

# make a few colors
black = (0,0,0)
blue = (0, 0, 150)
red = (255, 0, 0)
green = (0, 150, 0)
randRed = random.randint(0,255)
randGreen = random.randint(0,255)
randBlue = random.randint(0,255)
randColor = (randRed, randGreen, randBlue)
#draw a rectangle
pygame.draw.rect(screen,green,(200,100,50,50),15)
#Draw lines
point1 = (350,100)
point2 = (500,400)
pygame.draw.line(screen,red,point1,point2,7)
# draw circles
center = (400,300)
pygame.draw.circle(screen,randColor,center,50,5)
# update the display
pygame.display.update()

while (True):
    for event in pygame.event.get():
        # check to see if the user has closed the window
        if(event.type == QUIT):
            # end the program
            pygame.quit()
            sys.exit()