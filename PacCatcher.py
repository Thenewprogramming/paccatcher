import pygame
import Game
# from pygame.locals import *


class PacCatcher():
    """
    This is the mainmenu class of the game.
    """

    def __init__(self, screen, clock):
        self.clock = clock
        self.screen = screen
        pygame.display.set_caption("PacCathcer")
        self.quit = False
        self.mainloop()

    def mainloop(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitgame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.exitgame()
                    if event.key == pygame.K_g:
                        self.exitgame()
                    if event.key == pygame.K_s:
                        self.startgame(False, None)
                    if event.key == pygame.K_c:
                        self.startgame(True, "localhost")
            self.screen.fill((255, 255, 255))
            pygame.display.update()
            self.clock.tick(30)

    def exitgame(self):
        self.quit = True

    def startgame(self, isclient, serverip):
        Game.Game(isclient, serverip, self.screen, self.clock)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()
    PacCatcher(screen, clock)
