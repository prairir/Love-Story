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

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)
wintext = myfont.render('Congrats, You Made The Grilled Cheese', False, (0,0,0))
playtext = myfont.render('Make The Grilled Cheese', False, (0,0,0))
losetext = myfont.render('Sorry You Didnt Make The Grilled Cheese', False, (0,0,0))

class Top(pygame.sprite.Sprite):

    """The Top Piece for the grilled cheese that falls and can be controlled. """

    def __init__(self):
        self.y = 0
        self.x = display_height / 2
        self.image = topImg
        self.rect = 0
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.topx = 0
        self.topy = 0 

    def draw(self, x, y):
        screen.blit(topImg, (self.x + x, self.y + y))
        self.topx = ((self.x + x) - (self.width / 2) + 1)
        self.topy = ((self.y + y) - (self.height / 2) - 69)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))

class Bottom(pygame.sprite.Sprite):

    """The Bottom Piece for the grilled Cheese that stays still. """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.y = display_height - 100
        self.x = display_height / 2
        self.image = bottomImg
        self.rect = 0
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.topx = (self.x - (self.width / 2) + 1)
        self.topy = (self.y - (self.height / 2) + 1)

    def draw(self):
        screen.blit(bottomImg, (self.x, self.y))
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))
    
    def collidewith(self, ob):
        return self.rect.colliderect(ob)

if __name__ == "__main__":
    bottom = Bottom()
    top = Top()
    y = 0
    x = 0
    x_change = 0
    lose = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and not touching:
                    x_change = 3
                elif event.key == pygame.K_LEFT and not touching:
                    x_change = -3

            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_change = 0

        screen.fill(white)
        x += x_change
        bottom.draw()
        top.draw(x , y)
        touching = bottom.collidewith(top)
        if (top.y + y) > display_height:
            lose = True
        if not touching and not lose:
            screen.blit(playtext, (0,0))
            y +=1
        elif lose:
            screen.blit(losetext, (0,0))
        else:
            screen.blit(wintext, (0,0))
        pygame.display.update()
        clock.tick(120)
