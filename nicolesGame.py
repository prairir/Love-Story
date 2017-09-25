import pygame

pygame.init()

display_width = 800
display_height = 600
# colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('N + R = <3')
clock = pygame.time.Clock()

bunnyImg = pygame.image.load('data/images/bunny.png')


def bunny(x, y):
    gameDisplay.blit(bunnyImg, (x, y))

x = (display_width * 0.48)
y = (display_height * 0.48)

x_change = 0
y_change = 0

finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -4
            elif event.key == pygame.K_RIGHT:
                x_change = 4
            if event.key == pygame.K_UP:
                y_change = -4
            elif event.key == pygame.K_DOWN:
                y_change = 4

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT): 
                x_change = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                y_change = 0

    x += x_change
    y += y_change
    gameDisplay.fill(white)
    bunny(x, y + y_change)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
