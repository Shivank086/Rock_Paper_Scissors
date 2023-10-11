import pygame
import os
import random
pygame.init()

SCREEN_WIDTH = 1750
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("First Game")

def move(rect, x, y, i):
    if rect.left < 5 or rect.right > SCREEN_WIDTH-5:
        x = -x
    elif rect.top < 5 or rect.bottom > SCREEN_HEIGHT-5:
        y = -y
    varHold[i][2].left += x
    varHold[i][2].top += y
    varHold[i][3], varHold[i][4] = x, y

def placeCheck(rect1, rect2): return rect1.top<rect2.bottom and rect1.bottom>rect2.top and rect1.right>rect2.left and rect1.left<rect2.right
    
def typeCheck(img1, img2): return img1==img2+1 or img1 == img2-2


dim = 25
FPS = 20
vars = 40
varHold = []
for i in range(vars):
    varHold.append([3, pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ROCK.png')), (dim, dim)), 
                    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ROCK.png')), (dim, dim)).get_rect(), 8, 7])
for i in range(vars):
    varHold.append([2, pygame.transform.scale(pygame.image.load(os.path.join('assets', 'PAPER.png')), (dim, dim)), 
              pygame.transform.scale(pygame.image.load(os.path.join('assets', 'PAPER.png')), (dim, dim)).get_rect(), -6, -9])
for i in range(vars):
    varHold.append([1, pygame.transform.scale(pygame.image.load(os.path.join('assets', 'SCISSORS.png')), (dim, dim)), 
                pygame.transform.scale(pygame.image.load(os.path.join('assets', 'SCISSORS.png')), (dim, dim)).get_rect(), -1, 14])

for i in range(3*vars):
    varHold[i][2].topleft = (random.randint(dim, SCREEN_WIDTH-(2*dim)), random.randint(dim, SCREEN_HEIGHT-(2*dim)))
    varHold[i][3] = random.randint(-10, 10)
    while varHold[i][3] == 0:
        varHold[i][3] = random.randint(-10, 10)
    varHold[i][4] = random.randint(-10, 10)
    while varHold[i][4] == 0:
        varHold[i][4] = random.randint(-10, 10)


def listCheck():
    for i in range(3*vars-2):
        for j in range(3*vars-i):
            if placeCheck(varHold[i][2], varHold[j+i][2]) and typeCheck(varHold[i][0], varHold[j+i][0]):
                varHold[i][1] = varHold[j+i][1]
                varHold[i][0] = varHold[j+i][0]
            elif placeCheck(varHold[i+j][2], varHold[i][2]) and typeCheck(varHold[i+j][0], varHold[i][0]):
                varHold[i+j][1] = varHold[i][1]
                varHold[i+j][0] = varHold[i][0]


clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


    listCheck()


    screen.fill((0, 0, 0))
    for i in range(vars*3):
        screen.blit(varHold[i][1], varHold[i][2])
        move(varHold[i][2], varHold[i][3], varHold[i][4], i)
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
