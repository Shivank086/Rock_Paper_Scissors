import pygame
import os
import random
import math
pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900
x = 1
y = 1
X_SPEED = 3
Y_SPEED = 4
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("First Game")


ROCK_IMAGE = pygame.image.load(os.path.join('assets', 'ROCK.png'))
ROCK = pygame.transform.scale(ROCK_IMAGE, (25, 25))
rect = ROCK.get_rect()
"""
PAPER_IMAGE = pygame.image.load(os.path.join('assets', 'PAPER.png'))
PAPER = pygame.transform.scale(PAPER_IMAGE, (25, 25))
SCISSORS_IMAGE = pygame.image.load(os.path.join('assets', 'SCISSORS.png'))
SCISSORS = pygame.transform.scale(SCISSORS_IMAGE, (25, 25))
"""
FPS = 60


clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

        
        
    if rect.left<0 or rect.right>SCREEN_WIDTH:
        x *=-1
        X_SPEED = x*random.randint(1, 4)
        Y_SPEED = y*(5-X_SPEED)
    if rect.top<0 or rect.bottom>SCREEN_HEIGHT:
        y *=-1
        X_SPEED = x*random.randint(1, 4)
        Y_SPEED = y*(5-X_SPEED)
    rect.left += X_SPEED
    rect.top += Y_SPEED
    screen.fill((0, 0, 0))
    screen.blit(ROCK, rect)
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()