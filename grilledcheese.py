import pygame
import sys
import time

from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

display_width, display_height = 640, 480
screen = pygame.display.set_mode((display_width, display_height))
surface = pygame.Surface(screen.get_size())
white = (255,255,255)

pygame.display.set_caption('grilled cheese game')
topImg = pygame.image.load('data/images/topCheese.png')
bottomImg = pygame.image.load('data/images/bottomCheese.png')

class Top(pygame.sprite.Sprite):

    """Docstring for Top. """

    def __init__(self):
        """TODO: to be defined1. """

        self.y = 0
        self.x = display_height / 2
        self.image = topImg
        self.rect = self.image.get_rect()

    def draw(self, x, y):
        screen.blit(topImg, (self.x + x, self.y + y))
        

class Bottom(pygame.sprite.Sprite):

    """Docstring for Bottom. """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        """TODO: to be defined1. """
        self.y = display_height - 100
        self.x = display_height / 2
        self.image = bottomImg
        self.rect = self.image.get_rect()

    def draw(self):
        screen.blit(bottomImg, (self.x, self.y))

if __name__ == "__main__":
    bottom = Bottom()
    top = Top()
    y = 0
    x = 0
    x_change = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 3
                elif event.key == pygame.K_LEFT:
                    x_change = -3

            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_change = 0

        screen.fill(white)
        x += x_change
        bottom.draw()
        top.draw(x , y)
        if pygame.sprite.collide_rect(top, bottom):
            print("win")
        else: 
            y +=1
        pygame.display.update()
        clock.tick(120)
