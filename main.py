import sys, pygame
from pygame.locals import *                                # imports  all local files of the local directory
pygame.init()                                              # initiate all related internal pygame modules



size = width, height = 800, 900
speed = [2, 2]
black = 0, 0, 0                                            # RGB mode #000000 HEX_C

screen = pygame.display.set_mode(size)                     # make the screen;   (pygame.Surface object )

play = pygame.image.load("t.png")        
playrect = play.get_rect()                                 # get the rectangular coordinates of ball (pygame.Surface obj)

back = pygame.image.load("var.jpg")
screen.blit(back, (0,0) )
screen.blit(play,playrect)

for i in range(100):
    pygame.time.delay(100)                                 # time delay; so that we'd be able to see changes.
    screen.blit(back, playrect, playrect)                  # erasing the previous drawn play with placing back of same size there.
    playrect = playrect.move(2,0)                          # updating playrect on each loop
    screen.blit(play,playrect)
    pygame.display.flip()
    

while 1:
    for event in pygame.event.get():                       # Take care of all events happening.
        if event.type == pygame.QUIT: sys.exit()  

   


if __name__ == '__main__':
    main()

