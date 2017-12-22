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

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)
wintext = myfont.render('Congrats, You Got The Honey', False, (0,0,0))
playtext = myfont.render('Get The Honey Without Touching Bees', False, (0,0,0))
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

class Maze(object):

    """Docstring for Maze. """

    def __init__(self, image, x ,y ,rectx, recty):
        """TODO: to be defined1. """
        self.x = x
        self.y = y
        self.image = image
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rectx = rectx
        self.recty = recty

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        self.topx = ((self.x) - (self.width / 2) + self.rectx)
        self.topy = ((self.y) - (self.height /2) + self.recty)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))
        

def main():
    honey = Honey()
    bunny = Bunny()
    goal = Goal()
    bottom1 = Maze(bottom1Img, 0, display_height / 2 + 100, 55, 10)
    bottom2 = Maze(bottom2Img, 135, display_height / 2 + 165, 155, 13)
    top1 = Maze(top1Img, 0, display_height / 2 - 80, 100, -20)
    top2 = Maze(top2Img, 290, display_height/2 -80, 0, 0)
    top3 = Maze(top3Img, 280, display_height /2 - 9, 54, -20)
    top4 = Maze(top4Img, 424, 0, -10, 60)
    x, y = 0,0
    xHon, yHon = 0,0
    x_change = 0
    y_change = 0
    x_change_Honey, y_change_Honey = 0, 0
    finished = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and not finished:
                    x_change = 3
                    if honey.oktomove(bunny, goal):
                        x_change_Honey = 3
                elif event.key == pygame.K_LEFT and not finished:
                    x_change = -3
                    if honey.oktomove(bunny, goal):
                        x_change_Honey = -3
                if event.key == pygame.K_UP and not finished:
                    y_change = -3
                    if honey.oktomove(bunny, goal):
                        y_change_Honey = -3
                elif event.key == pygame.K_DOWN and not finished:
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
        if honey.collidewith(bunny) and honey.collidewith(goal):
            finished = True
            screen.blit(wintext,(0,0))
            break
        else:
            screen.blit(playtext, (0,0))
        pygame.display.update()
        clock.tick(120)
    return True
if __name__ == "__main__":
    print(main())
