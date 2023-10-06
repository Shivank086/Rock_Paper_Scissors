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
varHold = {
    "Rock": [3, ROCK, rect_R, Rx, Ry],
    "Paper": [2, PAPER, rect_P, Px, Py],
    "Scissors": [1, SCISSORS, rect_S, Sx, Sy]
}

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


    for i in range(len(varHold)-1):
        
        if i == len(varHold)-1: val = check(varHold[i+1][0], varHold[i+2][0])
        else: check(varHold[i+1][0], varHold[0][0])
        if val:
            varHold[i+1][0] = varHold[i+2][1]


    screen.fill((0, 0, 0))
    screen.blit(ROCK, rect_R)
    screen.blit(PAPER, rect_P)
    screen.blit(SCISSORS, rect_S)
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()