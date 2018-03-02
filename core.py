import sys
import pygame
import math
from colors import *

def swapBlock(a, b):
    a.color, b.color = b.color, a.color
    a.empty, b.empty = b.empty, a.empty

def drawGrid(gameobj, fall):
    for i in range(gameobj.cols):
        for b in gameobj.blocks[i]:
            pygame.draw.rect(gameobj.screen, b.color, [b.x, b.y ,b.w ,b.w])

    for i in range(fall.size):
        for j in range(fall.size):
            b = fall.blocks[i][j]
            if not b.empty:
                pygame.draw.rect(gameobj.screen, b.color, [b.x, b.y ,b.w ,b.w])

class game:
    def __init__(self, cols, rows, w):
        self.screen = pygame.display.set_mode(((w+1)*cols+1, (w+1)*rows+1))
        self.cols = cols
        self.rows = rows
        self.w = w
        self.finished = False
        self.blocks = [0] * self.cols
        for i in range(self.cols):
            self.blocks[i] = [0] * self.rows

    # start fresh grid
    def newBlocks(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.blocks[i][j] = block(i, j, self.w, GRAY, self)

    # check and destroy lines
    def checkLines(self):
        for row in range(self.rows):
            line = True
            for col in range(self.cols):
                if self.blocks[col][row].empty:
                    line = False
            if line:
                for r in range(row, self.rows-1):
                    for col in range(self.cols):
                        a = self.blocks[col][r]
                        a.empty = True
                        a.color = GRAY
                        b = self.blocks[col][r+1]
                        swapBlock(a, b)

class block:
    def __init__(self, i, j, w, color, gameobj):
        self.i = i
        self.j = j
        self.w = w
        self.color = color
        self.x = i * (w + 1) + 1
        self.y = (gameobj.rows - j -1) * (w + 1) + 1
        self.empty = True
        self.go = gameobj

    def updateXY(self):
        self.x = self.i * (self.w + 1) + 1
        self.y = (self.go.rows - self.j -1) * (self.w + 1) + 1

    # check if block can move here
    def validBlock(self):
        if self.i < 0 or self.i >= self.go.cols:
            return False
        if self.j < 0 or self.j >= self.go.rows:
            return False
        if not self.go.blocks[int(self.i)][int(self.j)].empty:
            return False
        return True
