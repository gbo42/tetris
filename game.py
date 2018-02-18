import sys, pygame
from core import *
from colors import *

#game setup
g = game()
g.newBlocks()
done = False

#size setup
height = (g.w+5)*g.rows-5
width = (g.w+5)*g.cols-5
size = (width, height)

#pygame config
pygame.init()
g.screen = pygame.display.set_mode(size)
pygame.display.set_caption("GT")
clock = pygame.time.Clock()

#main loop
while not done:
    #events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_LEFT:
                print('left()')
            elif event.key == pygame.K_RIGHT:
                print('right()')
            elif event.key == pygame.K_DOWN:
                print('down()')

    #graphics
    g.screen.fill((GRAY))
    drawGrid(g)
    pygame.display.flip()

    #framerate?
    clock.tick(60)

pygame.quit()
