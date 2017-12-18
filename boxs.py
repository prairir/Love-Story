import sys
import pygame
from pygame.locals import *

pygame.init()
clock=pygame.time.Clock()

display_width, display_height = 640, 480
screen = pygame.display.set_mode((display_width, display_height))
surface = pygame.Surface(screen.get_size())
white = (255, 255, 255)

pygame.display.set_caption('basic box prototype')
boxImg = pygame.image.load('data/images/box.png')
bunnyImg = pygame.image.load('data/images/bunny.png')
goalImg = pygame.image.load('data/images/goal.png')
pygame.key.set_repeat(1, 40) #checks the keys press (delay, interval)

class Box(object):

    """The Box object for a box moving game"""

    def __init__(self):
        """TODO: 
            check if touches goal
            """
        self.x = 40
        self.y = display_height - 140 
        self.image = boxImg
        self.rect = 0
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.topx = 0
        self.topy = 0

    def draw(self, x, y):
        screen.blit(boxImg, (self.x + x, self.y + y))
        self.topx = ((self.x + x) - (self.width / 2) + 1)
        self.topy = ((self.y + y) - (self.height / 2) - 30)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))

    def collidewith(self, ob):
        return self.rect.colliderect(ob)
    
    def okToMove(self, obb, obg):
        return self.collidewith(obb) and not self.collidewith(obg)
class Bunny(object):

    """The player for the game. """

    def __init__(self):
        """TODO:
        movement
        check when get to goal
        """
        self.x = 0
        self.y = display_height - 75
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

    """the object to get the boxes to the goal. """

    def __init__(self):
        """TODO: check if the box touches it. """
        self.x = display_width - 75
        self.y = display_height - 100
        self.image = goalImg
        self.rect = 0
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.topx = (self.x - (self.width / 2))
        self.topy = (self.y - (self.height / 2))

    def draw(self):
        screen.blit(goalImg, (self.x, self.y))
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))


def main():
    box = Box()
    bunny = Bunny()
    goal = Goal()
    x, y= 0, 0
    xBox, yBox = 0, 0
    x_change, y_change = 0 ,0 
    x_change_box, y_change_box = 0, 0
    score = 0
    iterator = 0
    boxes = [False, False, False, False, False]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 3
                    if box.okToMove(bunny, goal):
                        x_change_box = 3
                elif event.key == pygame.K_LEFT:
                    x_change = -3
                    if box.okToMove(bunny, goal):
                        x_change_box = -3
                if event.key == pygame.K_UP:
                    y_change = -3
                    if box.okToMove(bunny, goal):
                        y_change_box = -3
                elif event.key == pygame.K_DOWN:
                    y_change = 3
                    if box.okToMove(bunny, goal):
                        y_change_box = 3
                
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_change = 0 
                    x_change_box = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    y_change = 0
                    y_change_box = 0
        screen.fill(white)
        x += x_change
        y += y_change
        xBox += x_change_box
        yBox += y_change_box
        bunny.draw(x, y)
        box.draw(xBox,yBox)
        goal.draw()
        if box.collidewith(bunny) and box.collidewith(goal):
            boxes[iterator] = True
        if boxes[iterator]:
            score += 1
            xBox = 0
            yBox = 0
            iterator +=1
            print(iterator,  boxes)
        pygame.display.update()
        clock.tick(120)
    
if __name__ == "__main__":
    main()
