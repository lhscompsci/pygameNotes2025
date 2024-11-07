
import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((640,480))

white = (255,255,255)
screen.fill(white)

green = (0, 255, 0)
red = (255, 0 , 0)
x = (255, 0 , 255)
p1 = (50, 50)
p2 = (150, 100)
p3 = (300, 200)
p4 = (400, 200)
p5 = (500, 200)


                   #where to draw, color, point, radius, lineWidth
pygame.draw.circle(screen,         green,   p1,   15,        2)

                   #where to draw, color, point, radius, lineWidth
pygame.draw.circle(screen,          red,    p2,    30,       5)

                   #where to draw, color, point, radius, lineWidth
pygame.draw.circle(screen,          green,    p3,    50,       10)

                                                       #LINE WIDTH IS OPTIONAL
                   #where to draw, color, point, radius
pygame.draw.circle(screen,          red,    p4,    50)

                   #where to draw, color, point, radius
pygame.draw.circle(screen,          x,    p5,    10)

# update the screen
pygame.display.update()

while (True):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
              pygame.quit(); 
              sys.exit();