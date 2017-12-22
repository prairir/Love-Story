import pygame
import sys
from pygame.locals import *
import bees
import boxs
import grilledcheese as cheese

pygame.init()
clock = pygame.time.Clock()

display_width, display_height = 640, 480
screen = pygame.display.set_mode((display_width,display_height))
surface = pygame.Surface(screen.get_size())
pygame.display.set_caption('N + R = <3')
white = (255, 255, 255)

bunnyImg = pygame.image.load('data/images/bunny.png')
hedgeImg = pygame.image.load('data/images/hedgehog.png')
goalImg = pygame.image.load('data/images/goal.png')
pygame.display.set_icon(pygame.image.load('data/images/icon.png'))
pygame.key.set_repeat(1,40)

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)
class Bunny(object):

    """Docstring for Bunny. """

    def __init__(self, x, y):
        """TODO: to be defined1. """
        self.x = x
        self.y = y
        self.image = bunnyImg
        self.rect = 0
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.topx = 0
        self.topy = 0

    def draw(self,x , y):
        screen.blit(self.image, (self.x + x, self.y + y))
        self.topx = ((self.x + x) - (self.width / 2) -10)
        self.topy = ((self.y + y) - (self.height / 2)+1)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))
    
    def collidewith(self, ob):
        return self.rect.colliderect(ob)
        
class Hedge(object):

    """Docstring for hedge. """

    def __init__(self, x, y):
        """TODO: to be defined1. """
        self.x = x
        self.y = y
        self.image = hedgeImg
        self.rect = 0
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.topx = 0
        self.topy = 0

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        self.topx = ((self.x) - (self.width / 2) -10)
        self.topy = ((self.y) - (self.height / 2)+1)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))
    
    def collidewith(self, ob):
        return self.rect.colliderect(ob)
        
class Goal(object):

    """Docstring for Goal. """

    def __init__(self,x,y):
        """TODO: to be defined1. """
        self.x = x
        self.y = y
        self.image = goalImg
        self.rect = 0
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.topx = 0
        self.topy = 0

    def draw(self):
        screen.blit(self.image, (self.x , self.y))
        self.topx = ((self.x) - (self.width / 2) -10)
        self.topy = ((self.y) - (self.height / 2)+1)
        self.rect = pygame.Rect((self.topx, self.topy), (self.width, self.height))


def main():
    bunny = Bunny(5, display_height - 100)
    hedge = Hedge(display_width - 95, display_height - 100)
    goal1 = Goal(display_width / 2, display_height - 80)
    goal2 = Goal(display_width / 2 - 100, display_height - 80)
    goal3 = Goal(display_width / 2 + 100, display_height - 80)
    x, y = 0,0
    x_change, y_change = 0 ,0
    iterator = 0
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
                if event.key == pygame.K_UP:
                    y_change = -3
                elif event.key == pygame.K_DOWN:
                    y_change = 3

            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_change = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    y_change = 0

        screen.fill(white)
        x += x_change
        y += y_change
        if iterator == 0:
            bunny.draw(x, y)
            goal1.draw()
            hedge.draw()
            screen.blit(myfont.render('Move To HedgeHog', False, (0,0,0)), (0,0))
            if bunny.collidewith(goal1):
                screen.blit(myfont.render('At First Bunny Was Alone', False, (0,0,0)), (0,35))
            if bunny.collidewith(hedge):
                iterator += 1
                x = 0
                y = 0

        if iterator == 1:
            bunny.draw(x, y)
            goal2.draw()
            goal3.draw()
            hedge.draw()
            screen.blit(myfont.render('Move To HedgeHog', False, (0,0,0)), (0,0))
            if bunny.collidewith(goal2):
               screen.blit(myfont.render('Then She Met HedgeHog', False, (0,0,0)), (0,35))
            if bunny.collidewith(goal3):
                screen.blit(myfont.render('At First Things Were A Little Rocky', False, (0,0,0)), (0,35))
            if bunny.collidewith(hedge):
                iterator +=1
                x = 0
                y = 0

        if iterator == 2:
            bunny.draw(x,y)
            goal2.draw()
            goal3.draw()
            hedge.draw()
            screen.blit(myfont.render('Move To HedgeHog', False, (0,0,0)), (0,0))
            if bunny.collidewith(goal2):
                screen.blit(myfont.render('But Then They Fell Madly In Love', False, (0,0,0)), (0,35))
            if bunny.collidewith(goal3):
                screen.blit(myfont.render('Everything Was All Right', False, (0,0,0)), (0,35))
            if bunny.collidewith(hedge):
                iterator +=1 
                x = 0
                y = 0

        if iterator == 3:
            bunny.draw(x, y)
            goal1.draw()
            hedge.draw()
            screen.blit(myfont.render('Move To HedgeHog', False, (0,0,0)), (0,0))
            if bunny.collidewith(goal1):
                screen.blit(myfont.render('When They Cuddled They Were A Grilled Cheese', False, (0,0,0)), (0,35))

            if bunny.collidewith(hedge):
                iterator += 1
                cheese.main()
                x = 0
                y = 0
        
        if iterator ==4:
            bunny.draw(x, y)
            goal2.draw()
            goal3.draw()
            hedge.draw()
            screen.blit(myfont.render('Move To HedgeHog', False, (0,0,0)), (0,0))
            if bunny.collidewith(goal2):
                screen.blit(myfont.render('She Worked Hard', False, (0,0,0)), (0,35))
            if bunny.collidewith(goal3):
                screen.blit(myfont.render('She Came Home All Tired', False, (0,0,0)), (0,35))
            if bunny.collidewith(hedge):
                iterator +=1
                boxs.main()
                x = 0
                y = 0
                
        if iterator == 5:
            bunny.draw(x, y)
            goal2.draw()
            goal3.draw()
            hedge.draw()
            screen.blit(myfont.render('Move To HedgeHog', False, (0,0,0)), (0,0))
            if bunny.collidewith(goal2):
                screen.blit(myfont.render('It Made HedgeHog Sad', False, (0,0,0)), (0,35))
                screen.blit(myfont.render('To See Her Like This', False, (0,0,0)), (0,75))
            if bunny.collidewith(goal3):
                screen.blit(myfont.render('He Would Do Anything To Make Her Smile', False, (0,0,0)), (0,35))
            if bunny.collidewith(hedge):
                iterator +=1
                x = 0
                y = 0
        
        if iterator == 6:
            bunny.draw(x, y)
            goal2.draw()
            goal3.draw()
            hedge.draw()
            screen.blit(myfont.render('Move To HedgeHog', False, (0,0,0)), (0,0))
            if bunny.collidewith(goal2):
                screen.blit(myfont.render('In The Future She Will Start BeeKeeping', False, (0,0,0)), (0,35))
            if bunny.collidewith(goal3):
                screen.blit(myfont.render('She Will Be Super Good At It', False, (0,0,0)), (0,35))
            if bunny.collidewith(hedge):
                iterator +=1
                bees.main()
                x = 0
                y = 0

                
            

                


        pygame.display.update()
        clock.tick(120)

if __name__ == "__main__":
    main()
