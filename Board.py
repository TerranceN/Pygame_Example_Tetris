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
    def validate(self, shape, position):
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if not shape[j][i] == None:
                    pos = (position[0] + i, position[1] + j)
                    if pos[1] >= self.boardHeight: return 'placed'
                    if pos[0] < 0 or pos[0] >= self.boardWidth: return 'invalid'
                    if not self.board[pos[0]][pos[1]] == None: return 'placed'
        return "ok"
    def place(self, shape, position):
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if not shape[j][i] == None:
                    pos = (position[0] + i, position[1] + j)
                    self.board[pos[0]][pos[1]] = shape[j][i]
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
