import sys, pygame
from pygame.locals import *   # imports  all local files of the local directory
pygame.init()                 # initiate all related internal pygame modules



size = width, height = 800, 900
speed = [2, 2]
black = 0, 0, 0               # RGB mode #000000 HEX_C

screen = pygame.display.set_mode(size)            # make the screen;   (pygame.Surface object )

ball = pygame.image.load("intro_ball.gif")        
ballrect = ball.get_rect()                        # get the rectangular coordinates of ball (pygame.Surface obj)

while 1:
    for event in pygame.event.get():              # Take care of all events happening.
        if event.type == pygame.QUIT: sys.exit()  

    ballrect = ballrect.move(speed)               # simply changes the coordinates
    if ballrect.left < 0 or ballrect.right > width:     
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)                   # bitblt the pixels
    pygame.display.flip()                         # shows all changes at last

"""

if __name__ == '__main__':
    main()
"""
