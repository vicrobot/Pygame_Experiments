import pygame
from pygame.locals import *

def main():

    X, Y , A,B, vol = 150,200 , 50 ,70, 5
    pygame.init()
    player = pygame.image.load("t.png")
    background = pygame.image.load("logo.png")
    pygame.display.set_icon(player)
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("VicroBot")
    running = True
    screen.blit(background, (0,0))
    
    position = player.get_rect()
    screen.blit(player, position)          #draw the player
    pygame.display.update()                #and show it all
    for x in range(100):                   #animate 100 frames
        screen.blit(background, position, position) #erase
        position = position.move(2, 0)     #move player
        screen.blit(player, position)      #draw new player
        pygame.display.update()            #and show it all
        pygame.time.delay(100)

    """
    # main loop
    while running:
        pygame.time.delay(100)
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = 0
        v = pygame.key.get_pressed()
        if v[pygame.K_LEFT]:
            if X-vol >= 0:
                X -= vol

        if v[pygame.K_RIGHT]: 
            if X + A < 600:
                X += vol

        if v[pygame.K_UP]:
            if Y - vol >= 0: 
                Y -= vol

        if v[pygame.K_DOWN]:
            if Y + B< 600: 
                Y += vol
        if v[pygame.K_SPACE]:
            if Y - vol >= 0: 
                Y -= vol 
        #screen.fill((0,0,0))
        pygame.draw.rect(screen,(255,0,0),(X,Y,A,B))
        pygame.display.update()
"""
"""

import sys, pygame
pygame.init()

size = width, height = 800, 900
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("/home/ankit/intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

"""

if __name__ == '__main__':
    main()

