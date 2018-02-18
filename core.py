import sys, pygame
from colors import *

class game:
    def __init__(self):
        self.screen = 0
        self.cols = 10
        self.rows = 20
        self.w = 25
        self.blocks = [0] * self.cols
        for i in range(self.cols):
            self.blocks[i] = [0] * self.rows

    def newBlocks(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.blocks[i][j] = block(i, j, self.w, WHITE, self)

class block:
    def __init__(self, i, j, w, color, gameobj):
        self.i = i
        self.j = j
        self.w = w
        self.color = color

        self.x = i * (w + 5)
        self.y = (gameobj.rows - j -1) * (w + 5)

        self.empty = True

def drawGrid(gameobj):
    for i in range(gameobj.cols):
        for b in gameobj.blocks[i]:
            pygame.draw.rect(gameobj.screen, b.color, [b.x, b.y ,b.w ,b.w])

#for 4x4 matrices only
def rotate(matrix):
    for i in range(4):
        for j in range(i, 4):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(2):
        for j in range(4):
            matrix[i][j], matrix[3-i*2][j] = matrix[3-i*2][j], matrix[i][j]
