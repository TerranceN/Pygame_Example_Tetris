import pygame

from GameState import *
from InputHandler import *

class GS_Game(GameState):
    inputHandler = InputHandler()
    def handleEvent(self, event):
        self.inputHandler.handleEvent(event);
    def update(self):
        if self.inputHandler.isKeyDown(pygame.K_ESCAPE):
            self.isAlive = False
