import pygame
import os
import random
import math
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
Rx = 8
Ry = 6

Px = -4
Py = -9

Sx = -1
Sy = 10
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("First Game")
def switch(fir, sec):
    z=fir
    fir=-sec
    sec=z
    return fir, sec

def move(rect, x, y):
    if rect.left<0 or rect.right>SCREEN_WIDTH:
        x = -x
    if rect.top<0 or rect.bottom>SCREEN_HEIGHT:
        y = -y
    rect.left += x
    rect.top += y
    return x, y

def check(rect1, rect2):
    if rect1.top<rect2.bottom and rect1.bottom>rect2.top and rect1.right>rect2.left and rect1.left<rect2.right:
        return True
    return False

dim = 100
ROCK = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ROCK.png')), (dim, dim))
rect_R = ROCK.get_rect()
rect_R.topleft = (dim, dim)


PAPER = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'PAPER.png')), (dim, dim))
rect_P = PAPER.get_rect()
rect_P.topleft = (SCREEN_WIDTH-dim, SCREEN_HEIGHT-dim)

SCISSORS = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'SCISSORS.png')), (dim, dim))
rect_S = SCISSORS.get_rect()
rect_S.topleft = (SCREEN_WIDTH-dim, dim)

FPS = 30

clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

        
    hold = move(rect_R, Rx, Ry)
    Rx, Ry = hold[0], hold[1]
    
    hold = move(rect_P, Px, Py)
    Px, Py = hold[0], hold[1]
    
    hold = move(rect_S, Sx, Sy)
    Sx, Sy = hold[0], hold[1]


    if check(rect_R, rect_S):
        SCISSORS = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ROCK.png')), (dim, dim))

    if check(rect_S, rect_P):
        PAPER = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'SCISSORS.png')), (dim, dim))

    if check(rect_P, rect_R):
        ROCK = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'PAPER.png')), (dim, dim))

    screen.fill((0, 0, 0))
    screen.blit(ROCK, rect_R)
    screen.blit(PAPER, rect_P)
    screen.blit(SCISSORS, rect_S)
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()