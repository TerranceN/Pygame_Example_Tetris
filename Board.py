import pygame
import copy

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
        for i in range(self.boardHeight):
            self.board.append([])
            for j in range(self.boardWidth):
                self.board[i].append(None)
    def validate(self, shape, position):
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if not shape[i][j] == None:
                    pos = (position[0] + j, position[1] + i)
                    if pos[1] >= self.boardHeight: return 'placed'
                    if pos[0] < 0 or pos[0] >= self.boardWidth: return 'invalid'
                    if not self.board[pos[1]][pos[0]] == None: return 'placed'
        return "ok"
    def place(self, shape, position):
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if not shape[i][j] == None:
                    pos = (position[0] + j, position[1] + i)
                    self.board[pos[1]][pos[0]] = shape[i][j]
        for i in range(len(shape)):
            isNotEmpty = False
            for j in range(len(shape[i])):
                if not shape[i][j] == None:
                    isNotEmpty = True
            if isNotEmpty:
                self.checkForFilledRow(position[1] + i)
    def checkForFilledRow(self, row):
        for j in range(len(self.board[row])):
            if self.board[row][j] == None: return
        for currentRow in self.__reverseList(range(row)):
            for j in range(len(self.board[currentRow])):
                self.board[currentRow+1][j] = self.board[currentRow][j]
    def draw(self, display):
        for i in range(self.boardHeight):
            for j in range(self.boardWidth):
                self.drawBlock(
                        display,
                        self.board[i][j],
                        (j * self.tileSize, i * self.tileSize))
    def drawBlock(self, display, name, position):
        block = self.__getBlock(name)
        if not block == None:
            display.blit(self.__getBlock(name).image, position)
    def __getBlock(self, name):
        for block in self.blocks:
            if block.name == name:
                return block
    def __reverseList(self, lst):
        newLst = copy.deepcopy(lst)
        newLst.reverse()
        return newLst
