import sys
import pygame
import random
from core import *
from faller import *

# game objects and settings
g = game(10, 20, 25)
g.newBlocks()
f = Faller(g)
f.newBlocks(random.choice(minos))
FALLEVENT = pygame.USEREVENT+1

# pygame setup
pygame.init()
pygame.time.set_timer(FALLEVENT, 500)
pygame.display.set_caption("GT")
clock = pygame.time.Clock()

# falling event handlers
def fall(f):
    if (f.canMove(0, -1)):
        f.move(0, -1)
    else:
        f.lockToGrid()
        f.newBlocks(random.choice(minos))
        if (not f.canMove(0, 0)):
            g.finished = True

# key event handler
def keyPressed(ekey):
    if ekey == pygame.K_ESCAPE:
        g.finished = True
    elif ekey == pygame.K_LEFT:
        if(f.canMove(-1, 0)):
            f.move(-1, 0)
    elif ekey == pygame.K_RIGHT:
        if(f.canMove(1, 0)):
            f.move(1, 0)
    elif ekey == pygame.K_DOWN:
        if(f.canMove(0, -1)):
            f.move(0, -1)
    elif ekey == pygame.K_UP:
        if(f.canRotate()):
            f.rotate()
    elif ekey == pygame.K_SPACE:
        while (f.canMove (0,-1)):
            f.move(0, -1)

# main loop
while not g.finished:
    # checks
    g.checkLines()

    # event handler
    for event in pygame.event.get():
        if event.type == FALLEVENT:
            fall(f)
        if event.type == pygame.QUIT:
            g.finished = True
        elif event.type == pygame.KEYDOWN:
            keyPressed(event.key)

    # render
    g.screen.fill((WHITE))
    drawGrid(g, f)
    pygame.display.flip()

# exit game
pygame.quit()
