import sys
import pygame
import math
from colors import *
from core import *

class Faller:
    def __init__(self, gobj):
        self.go = gobj
        self.size = 4
        self.blocks = [0] * self.size
        for i in range(self.size):
            self.blocks[i] = [0] * self.size

    # create new falling piece piece
    def newBlocks(self, mino):
        self.size = mino['size']
        for i in range(self.size):
            for j in range(self.size):
                colOff = math.floor(self.go.cols/2)
                rowOff = math.floor(self.go.rows+2)
                self.blocks[i][j] = block(i + colOff, rowOff-j, self.go.w, GRAY, self.go)
                if mino['grid'][j][i] == 1:
                    self.blocks[i][j].empty = False
                    self.blocks[i][j].color = mino['color']
                else:
                    self.blocks[i][j].empty = True

    # rotate piece
    def rotate(self):
        for i in range(self.size):
            for j in range(i, self.size):
                a = self.blocks[i][j]
                b = self.blocks[j][i]
                swapBlock(a, b)

        for j in range(self.size):
            for i  in range(math.floor(self.size/2)):
                a = self.blocks[i][j]
                b = self.blocks[(self.size-1)-i][j]
                swapBlock(a, b)

    # check if rotation is possible
    def canRotate(self):
        for i in range(self.size):
             for j in range(i, self.size):
                 a = self.blocks[i][j]
                 b = self.blocks[j][i]
                 if not (a.empty or b.validBlock()):
                     return False
                 if not (b.empty or a.validBlock()):
                     return False

        for j in range(self.size):
            for i  in range(math.floor(self.size/2)):
                a = self.blocks[i][j]
                b = self.blocks[(self.size-1)-i*2][j]
                if not (a.empty or b.validBlock()):
                    return False
                if not (b.empty or a.validBlock()):
                    return False
        return True

    #check if movement is possible
    def canMove(self, i, j):
        for col in range(self.size):
            for row in range (self.size):
                b = self.blocks[col][row]
                if (b.i+i < 0 or b.i+i >= self.go.cols or b.j + j < 0) and not b.empty:
                    return False
                if not b.empty and b.j+j < self.go.rows:
                    if not self.go.blocks[b.i + i][b.j+j].empty:
                        return False

        return True

    # move piece
    def move(self, i, j):
        for col in range(self.size):
            for row in range (self.size):
                b = self.blocks[col][row]
                b.i += i
                b.j += j
                b.updateXY()

    # lock piece in place
    def lockToGrid(self):
        for col in range(self.size):
            for row in range (self.size):
                b = self.blocks[col][row]
                if not b.empty:
                    a = self.go.blocks[b.i][b.j]
                    swapBlock(a, b)
