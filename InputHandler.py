import pygame

class InputHandler:
    keysDown = []
    keysDownOnce = []
    def isKeyDown(self, key):
        return self.keysDown.count(key) > 0
    def isKeyHit(self, key):
        if self.keysDown.count(key) > 0 :
            if self.keysDownOnce.count(key) > 0:
                self.keysDownOnce = self.__remove(self.keysDownOnce, key)
                return True
        return False
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            self.__keyDown(event.key)
        elif event.type == pygame.KEYUP:
            self.__keyUp(event.key)
    def __keyUp(self, key):
        self.keysDown = self.__remove(self.keysDown, key);
        self.keysDownOnce = self.__remove(self.keysDownOnce, key);
    def __keyDown(self, key):
        if self.keysDown.count(key) == 0:
            self.keysDown.append(key)
            self.keysDownOnce.append(key)
    def __remove(self, lst, key):
        newKeys = []
        for currentKey in self.keysDown:
            if currentKey != key:
                newKeys.append(currentKey)
        return newKeys
