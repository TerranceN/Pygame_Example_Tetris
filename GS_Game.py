import pygame

from GameState import *
from InputHandler import *
from Board import *
from Shape import *

class GS_Game(GameState):
    inputHandler = InputHandler()
    board = None
    shape = None
    movementTime = 0
    def __init__(self, display):
        GameState.__init__(self, display)
        self.board = Board()
        self.shape = Shape(self.board,
                [['cyan', 'cyan', 'cyan']
                ,[None, 'cyan', None]
                ,[None, None, None]])
    def handleEvent(self, event):
        self.inputHandler.handleEvent(event)
    def update(self):
        if self.inputHandler.isKeyDown(pygame.K_ESCAPE):
            self.isAlive = False
        if self.inputHandler.isKeyHit(pygame.K_s):
            self.shape.move((0, 1))
        if self.inputHandler.isKeyHit(pygame.K_a):
            self.shape.move((-1, 0))
        if self.inputHandler.isKeyHit(pygame.K_d):
            self.shape.move((1, 0))
        if pygame.time.get_ticks() > self.movementTime:
            self.shape.move((0, 1))
            self.movementTime = pygame.time.get_ticks() + 200
    def draw(self):
        self.board.draw(self.display)
        self.shape.draw(self.display)
