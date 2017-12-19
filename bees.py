import sys
import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

display_width, display_height = 640, 480
screen = pygame.display.set_mode((display_width, display_height))
surface = pygame.Surface(screen.get_size())
white = (255,255,255)

pygame.display.set_caption('bee game')
beeImg = pygame.image.load('data/images/bee.png')
bunnyImg = pygame.image.load('data/images/bunny.png')
honeyImg = pygame.image.load('data/images/honey.png')
goalImg = pygame.image.load('data/images/goal.png')
pygame.key.set_repeat(1,40)

class Honey(object):

    """Docstring for Honey. """

    def __init__(self):
        """TODO: 
            check touching bunny
            check touching goal
            check movement  
            """
        self.x = display_width - 80
        self.y = display_height / 2
        self.image = honeyImg
        self.rect = 0 
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.topx = 0
        self.topy = 0


    def draw(self, x, y):
        screen.blit(honeyImg, (self.x + x, self.y + y))
        self.topx = ((self.x + x) - (self.width / 2) + 1)
        self.topy = ((self.y + y) - (self.height / 2) + 1)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))

    def collidewith(self, ob):
        return self.rect.colliderect(ob)

