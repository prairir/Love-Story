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
top1Img = pygame.image.load('data/images/top1.png')
top2Img = pygame.image.load('data/images/top2.png')
top3Img = pygame.image.load('data/images/top3.png')
top4Img = pygame.image.load('data/images/top4.png')
bottom1Img = pygame.image.load('data/images/bottom1.png')
bottom2Img = pygame.image.load('data/images/bottom2.png')
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
        self.y =   0
        self.image = honeyImg
        self.rect = 0 
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.topx = 0
        self.topy = 0


    def draw(self, x, y):
        screen.blit(honeyImg, (self.x + x, self.y + y))
        self.topx = ((self.x + x) - (self.width / 2) + 40)
        self.topy = ((self.y + y) - (self.height / 2) - 10)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))

    def collidewith(self, ob):
        return self.rect.colliderect(ob)

    def oktomove(self, ob1, ob2):
        return self.collidewith(ob1) and not self.collidewith(ob2)

class Bunny(object):

    """Docstring for Bunny. """

    def __init__(self):
        """TODO: 
            movement 
            """
        self.x = 75
        self.y = display_height / 2
        self.image = bunnyImg
        self.rect = 0
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.topx = 0
        self.topy = 0

    def draw(self, x, y):
        screen.blit(bunnyImg, (self.x + x, self.y + y))
        self.topx = ((self.x + x) - (self.width / 2) + 1)
        self.topy = ((self.y + y) - (self.height / 2) + 1)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))

    def collidewith(self, ob):
        return self.rect.colliderect(ob)

class Goal(object):

    """Docstring for Goal. """

    def __init__(self):
        """TODO: check if honey gets to goal. """
        self.x = 0
        self.y = display_height / 2
        self.image = goalImg
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.topx = ((self.x) - (self.width / 2) + 1)
        self.topy = ((self.y) - (self.height / 2) + 1)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))

    def draw(self):
        screen.blit(goalImg, (self.x, self.y))


class Top1(object):

    """Docstring for Bee. """

    def __init__(self):
        """TODO: to be defined1. """
        self.x = 0
        self.y = display_height / 2 - 80 
        self.image = top1Img
        self.height = self.image.get_height()
        self.width = self.image.get_width()

    def draw(self):
        screen.blit(top1Img, (self.x, self.y))
        self.topx = ((self.x) - (self.width / 2) + 100)
        self.topy = ((self.y) - (self.height / 2) - 20)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))

class Top2(object):

    """Docstring for Bee. """

    def __init__(self):
        """TODO: to be defined1. """
        self.x = 290
        self.y = display_height / 2 - 80 
        self.image = top2Img
        self.height = self.image.get_height()
        self.width = self.image.get_width()

    def draw(self):
        screen.blit(top2Img, (self.x, self.y))
        self.topx = ((self.x) - (self.width / 2))
        self.topy = ((self.y) - (self.height / 2)) 
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))

class Top3(object):

    """Docstring for Bee. """

    def __init__(self):
        """TODO: to be defined1. """
        self.x = 280
        self.y = display_height / 2 - 9  
        self.image = top3Img
        self.height = self.image.get_height()
        self.width = self.image.get_width()

    def draw(self):
        screen.blit(top3Img, (self.x, self.y))
        self.topx = ((self.x) - (self.width / 2)+ 54)
        self.topy = ((self.y) - (self.height / 2) - 20) 
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))

class Top4(object):

    """Docstring for Bee. """

    def __init__(self):
        """TODO: to be defined1. """
        self.x = 424
        self.y =  0 
        self.image = top4Img
        self.height = self.image.get_height()
        self.width = self.image.get_width()

    def draw(self):
        screen.blit(top4Img, (self.x, self.y))
        self.topx = ((self.x) - (self.width / 2) - 10)
        self.topy = ((self.y) - (self.height / 2) + 60) 
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))

class Bottom1(object):

    """Docstring for Bee. """

    def __init__(self):
        """TODO: to be defined1. """
        self.x = 0
        self.y = display_height / 2 + 100
        self.image = bottom1Img
        self.height = self.image.get_height()
        self.width = self.image.get_width()

    def draw(self):
        screen.blit(bottom1Img, (self.x, self.y))
        self.topx = ((self.x) - (self.width / 2) + 65)
        self.topy = ((self.y) - (self.height / 2) + 10)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))

class Bottom2(object):

    """Docstring for Bee. """

    def __init__(self):
        """TODO: to be defined1. """
        self.x = 135
        self.y = display_height / 2 + 165
        self.image = bottom2Img
        self.height = self.image.get_height()
        self.width = self.image.get_width()

    def draw(self):
        screen.blit(bottom2Img, (self.x, self.y))
        self.topx = ((self.x) - (self.width / 2) + 155)
        self.topy = ((self.y) - (self.height / 2) + 13)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))

def main():
    honey = Honey()
    bunny = Bunny()
    goal = Goal()
    bottom1 = Bottom1()
    bottom2 = Bottom2()
    top1 = Top1()
    top2 = Top2()
    top3 = Top3()
    top4 = Top4()
    x, y = 0,0
    xHon, yHon = 0,0
    x_change = 0
    y_change = 0
    x_change_Honey, y_change_Honey = 0, 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 3
                    if honey.oktomove(bunny, goal):
                        x_change_Honey = 3
                elif event.key == pygame.K_LEFT:
                    x_change = -3
                    if honey.oktomove(bunny, goal):
                        x_change_Honey = -3
                if event.key == pygame.K_UP:
                    y_change = -3
                    if honey.oktomove(bunny, goal):
                        y_change_Honey = -3
                elif event.key == pygame.K_DOWN:
                    y_change = 3
                    if honey.oktomove(bunny, goal):
                        y_change_Honey = 3

            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_change = 0
                    x_change_Honey = 0
                if event.key in (pygame.K_DOWN, pygame.K_UP):
                    y_change = 0
                    y_change_Honey = 0

        screen.fill(white)
        x += x_change
        y += y_change
        xHon += x_change_Honey
        yHon += y_change_Honey
        bunny.draw(x,y)
        honey.draw(xHon,yHon)
        top1.draw()
        top2.draw()
        top3.draw()
        top4.draw()
        bottom1.draw()
        bottom2.draw()
        goal.draw()
        if bunny.collidewith(top1) or bunny.collidewith(top2) or bunny.collidewith(top3) or bunny.collidewith(top4) or bunny.collidewith(bottom1) or bunny.collidewith(bottom2):
            x = 0
            y = 0
        pygame.display.update()
        clock.tick(120)

if __name__ == "__main__":
    main()
