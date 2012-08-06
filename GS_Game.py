import pygame

import random

from GameState import GameState
from InputHandler import InputHandler
from Board import Board
from Shape import Shape


class GS_Game(GameState):
    inputHandler = InputHandler()
    board = None
    shape = None
    movementTime = 0

    def __init__(self, display):
        GameState.__init__(self, display)
        self.board = Board()
        self.shape = Shape(self.board, self.randomShape())

    def handleEvent(self, event):
        self.inputHandler.handleEvent(event)

    def update(self):
        if self.inputHandler.isKeyDown(pygame.K_ESCAPE):
            self.isAlive = False
        if self.inputHandler.isKeyHit(pygame.K_w):
            self.shape.rotateCW()
        if self.inputHandler.isKeyHit(pygame.K_s):
            self.shape.move((0, 1))
        if self.inputHandler.isKeyHit(pygame.K_a):
            self.shape.move((-1, 0))
        if self.inputHandler.isKeyHit(pygame.K_d):
            self.shape.move((1, 0))
        if pygame.time.get_ticks() > self.movementTime:
            self.shape.move((0, 1))
            self.movementTime = pygame.time.get_ticks() + 200
        if self.shape.isPlaced:
            self.shape = Shape(self.board, self.randomShape())

    def draw(self):
        self.board.draw(self.display)
        self.shape.draw(self.display)

    def randomShape(self):
        randInt = random.randint(1, 7)
        if randInt == 1:
            return  [['yellow', 'yellow'],
                     ['yellow', 'yellow']]
        elif randInt == 2:
            return  [['purple', 'purple', 'purple'],
                     [None, 'purple', None],
                     [None, None, None]]
        elif randInt == 3:
            return  [['red', 'red', None],
                     [None, 'red', 'red'],
                     [None, None, None]]
        elif randInt == 4:
            return  [[None, 'green', 'green'],
                     ['green', 'green', None],
                     [None, None, None]]
        elif randInt == 5:
            return  [[None, None, 'orange'],
                     ['orange', 'orange', 'orange'],
                     [None, None, None]]
        elif randInt == 6:
            return  [['blue', None, None],
                     ['blue', 'blue', 'blue'],
                     [None, None, None]]
        elif randInt == 7:
            return  [[None, None, None, None],
                     ['cyan', 'cyan', 'cyan', 'cyan'],
                     [None, None, None, None],
                     [None, None, None, None]]
