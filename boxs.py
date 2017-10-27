import pygame
import time
import sys

from pygame.locals import *

pygame.init()
clock=pygame.time.Clock()

display_width, display_height = 640, 480
screen = pygame.display.set_mode((display_width, display_height))
surface = pygame.Surface(screen.get_size()) 
pygame.display.set_caption('basic box prototype')

pygame.key.set_repeat(1, 40) #checks the keys press (delay, interval)

class Box(object):

    """The Box object for a box moving game"""

    def __init__(self):
        """TODO: to be defined1. """

if __name__ == "__main__":
       box = Box()

       while True:

           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()

           clock.tick(120)
