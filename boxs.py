import sys
import time
import pygame

from pygame.locals import *

pygame.init()
clock=pygame.time.Clock()

display_width, display_height = 640, 480
screen = pygame.display.set_mode((display_width, display_height))
surface = pygame.Surface(screen.get_size())

pygame.display.set_caption('basic box prototype')
boxImg = pygame.image.load('data/images/box.png')
bunnyImg = pygame.image.load('data/images/bunny.png')
pygame.key.set_repeat(1, 40) #checks the keys press (delay, interval)

class Box(object):

    """The Box object for a box moving game"""

    def __init__(self):
        """TODO: 
            movement with the bunny if they are touching. 
            check if touches bunny
            check if touches goal
            """
        self.posX = 0
        self.posY = 60

    def draw(self, x, y):
        screen.blit(boxImg, (self.posX + x, self.posY + y))

class Nicole(object):

    """The player for the game. """

    def __init__(self):
        """TODO: 
        movement
        check to touch the box
        check when get to goal
        """
        
class Goal(object):

    """the object to get the boxes to the goal. """

    def __init__(self):
        """TODO: check if the box touches it. """
        
if __name__ == "__main__":
    box = Box()
    box.draw(0, 0)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(120)
