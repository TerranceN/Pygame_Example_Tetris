import pygame

class Block:
    image = None
    name = None
    def __init__(self, name):
        self.name = name
        self.image = pygame.image.load('block_' + name + '.png')

class Board:
    tileSize = 20
    boardWidth = 10
    boardHeight = 20
    board = []
    blocks = []
    def __init__(self):
        self.blocks.append(Block('red'))
        self.blocks.append(Block('purple'))
        self.blocks.append(Block('green'))
        self.blocks.append(Block('yellow'))
        self.blocks.append(Block('orange'))
        self.blocks.append(Block('blue'))
        self.blocks.append(Block('cyan'))
        for i in range(self.boardWidth):
            self.board.append([])
            for j in range(self.boardHeight):
                self.board[i].append(None)
    def update(self):
        pass
    def draw(self, display):
        for i in range(self.boardWidth):
            for j in range(self.boardHeight):
                self.drawBlock(
                        display,
                        self.board[i][j],
                        (i * self.tileSize, j * self.tileSize))
    def drawBlock(self, display, name, position):
        block = self.__getBlock(name)
        if not block == None:
            display.blit(self.__getBlock(name).image, position)
    def __getBlock(self, name):
        for block in self.blocks:
            if block.name == name:
                return block
