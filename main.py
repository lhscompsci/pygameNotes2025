import pygame
import random
import sys

from pygame.locals import *

print(random.randint(1, 100))
# a random integer in the closed interval [1,100]

print(random.random())
# a random number between 0.0 and 1.0

# create the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))

# color in the screen white
white = (255, 255, 255)
blue = (0, 0, 150)
red = (255, 0, 0)
green = (0, 150, 0)
randRed = random.randint(0,255)
randGreen = random.randint(0,255)
randBlue = random.randint(0,255)
randColor = (randRed, randGreen, randBlue)
screen.fill(randColor)

# update the display
pygame.display.update()

while (True):
    for event in pygame.event.get():
        # check to see if the user has closed the window
        if(event.type == QUIT):
            # end the program
            pygame.quit()
            sys.exit()