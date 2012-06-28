import pygame

class Block:
    image = None
    name = None
    def __init__(self, name):
        self.name = name
        self.image = pygame.image.load('block_' + name + '.png')

class Board:
    boardWidth = 10
    boardHeight = 20
    blocks = []
    def __init__(self):
        self.blocks.append(Block('red'))
        self.blocks.append(Block('purple'))
        self.blocks.append(Block('green'))
        self.blocks.append(Block('yellow'))
        self.blocks.append(Block('orange'))
        self.blocks.append(Block('blue'))
        self.blocks.append(Block('cyan'))
    def update(self):
        pass
    def draw(self, display):
        self.drawBlock(display, 'green', (0, 0))
    def drawBlock(self, display, name, position):
        display.blit(self.__getBlock(name).image, position)
    def __getBlock(self, name):
        for block in self.blocks:
            if block.name == name:
                return block
