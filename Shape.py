import pygame

from Board import *

class Shape:
    shape = None
    board = None
    position = (3, 0)
    isPlaced = False
    def __init__(self, board, shape):
        self.board = board
        self.shape = shape
    def update(self):
        pass
    def draw(self, display):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                pos = ((self.position[0] + j) * self.board.tileSize,
                       (self.position[1] + i) * self.board.tileSize)
                self.board.drawBlock(
                        display,
                        self.shape[i][j],
                        pos)
    def move(self, delta):
        prePosition = self.position
        self.position = (self.position[0] + delta[0], self.position[1] + delta[1])
        result = self.board.validate(self.shape, self.position)
        if not result == 'ok':
            self.position = prePosition
            if delta[1] > 0 and result == 'placed':
                self.board.place(self.shape, self.position)
                self.isPlaced = True
                self.position = (3, 0)
    def rotateCW(self):
        pass
    def rotateCCW(self):
        for i in range(3) : self.rotateCW()
