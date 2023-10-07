import pygame
import os
import random
import math
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("First Game")
def switch(fir, sec):
    z=fir
    fir=-sec
    sec=z
    return fir, sec

def move(rect, x, y, i):
    holdx = abs(x)/x
    holdy = abs(y)/y
    if rect.left<0 or rect.right>SCREEN_WIDTH:
        x = holdx*random.randint(1, 10)
        y = holdy*(10-abs(x))
    if rect.top<0 or rect.bottom>SCREEN_HEIGHT:
        y = holdy*random.randint(1, 10)
        x = holdx*(10-abs(y))
    varHold[keyHold[i]][2].left += x
    varHold[keyHold[i]][2].top += y
    varHold[keyHold[i]][3], varHold[keyHold[i]][4] = x, y

def placeCheck(rect1, rect2):
    if rect1.top<rect2.bottom and rect1.bottom>rect2.top and rect1.right>rect2.left and rect1.left<rect2.right: return True
    return False

def typeCheck(img1, img2):
    if img1==img2+1 or img1 == img2-2:return True
    return False


dim = 100
FPS = 30
varHold = {
    "Rock": [3, pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ROCK.png')), (dim, dim)), 
             pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ROCK.png')), (dim, dim)).get_rect(), 8, 7],
    "Paper": [2, pygame.transform.scale(pygame.image.load(os.path.join('assets', 'PAPER.png')), (dim, dim)), 
              pygame.transform.scale(pygame.image.load(os.path.join('assets', 'PAPER.png')), (dim, dim)).get_rect(), -6, -9],
    "Scissors": [1, pygame.transform.scale(pygame.image.load(os.path.join('assets', 'SCISSORS.png')), (dim, dim)), 
                 pygame.transform.scale(pygame.image.load(os.path.join('assets', 'SCISSORS.png')), (dim, dim)).get_rect(), -1, 14]
}
keyHold = list(varHold.keys())
varHold[keyHold[0]][2].topleft = (dim, dim)
varHold[keyHold[1]][2].topleft = (SCREEN_WIDTH-dim, SCREEN_HEIGHT-dim)
varHold[keyHold[2]][2].topleft = (SCREEN_WIDTH-dim, dim)

def listCheck():
    for i in range(len(keyHold)-2):
        for j in range(len(keyHold)-(i+1)):
            if placeCheck(varHold[keyHold[i+1]][2], varHold[keyHold[j+i+1]][2]) and typeCheck(varHold[keyHold[i+1]][0], varHold[keyHold[j+i+1]][0]):
                varHold[keyHold[i+1]][1] = varHold[keyHold[j+i+1]][1]
                varHold[keyHold[i+1]][0] = varHold[keyHold[j+i+1]][0]


clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


    listCheck()


    screen.fill((0, 0, 0))
    for i in range(len(keyHold)):
        screen.blit(varHold[keyHold[i]][1], varHold[keyHold[i]][2])
        move(varHold[keyHold[i]][2], varHold[keyHold[i]][3], varHold[keyHold[i]][4], i)
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()