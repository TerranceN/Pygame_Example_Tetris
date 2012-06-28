import pygame

from Board import *

class Shape:
    shape = None
    board = None
    position = (3, 0)
    def __init__(self, board, shape):
        self.board = board
        self.shape = shape
    def update(self):
        pass
    def draw(self, display):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                pos = ((self.position[0] + i) * self.board.tileSize,
                       (self.position[1] + j) * self.board.tileSize)
                self.board.drawBlock(
                        display,
                        self.shape[j][i],
                        pos)
    def move(self, delta):
        self.position = (self.position[0] + delta[0], self.position[1] + delta[1])
    def rotateCW(self):
        pass
    def rotateCCW(self):
        for i in range(3) : self.rotateCW()
