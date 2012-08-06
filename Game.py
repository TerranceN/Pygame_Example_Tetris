import pygame

from GS_Game import GS_Game


class Game:
    gamestateStack = []
    display = None
    clock = None
    isRunning = True

    def __init__(self):
        """
        initialize game:
            init pygame,
            create window,
            create clock,
            add first gamestate
        """
        pygame.init()
        self.display = pygame.display.set_mode([200, 400])
        self.clock = pygame.time.Clock()
        self.gamestateStack.append(GS_Game(self.display))

    def run(self):
        """
        run game:
            handle events
            update and draw game
            delay to lock game at 60 fps
        """
        while self.isRunning and len(self.gamestateStack) > 0:
            self.handleEvents()
            self.update()
            self.draw()
            if not self.gamestateStack[len(self.gamestateStack) - 1].isAlive:
                self.gamestateStack.pop()
            self.clock.tick(60)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
            self.gamestateStack[len(self.gamestateStack) - 1].handleEvent(event)

    def update(self):
        self.gamestateStack[len(self.gamestateStack) - 1].update()

    def draw(self):
        self.display.fill((0, 0, 0))
        self.gamestateStack[len(self.gamestateStack) - 1].draw()
        pygame.display.flip()
