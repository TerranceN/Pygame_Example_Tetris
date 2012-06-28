import pygame

class GameState:
    display = None
    isAlive = True
    def __init__(self, display):
        self.display = display
    def handleEvent(self, event):
        pass
    def update(self):
        pass
    def draw(self):
        pass
