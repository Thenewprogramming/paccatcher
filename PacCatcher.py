import pygame
import Server
import threading
import Client
import Game
# from pygame.locals import *

class PacCatcher():
    
    def __init__(self, screen, clock):
        self.clock = clock
        self.screen = screen
        self.quit = False
        self.returnmsg = ""
        self.mainloop()
#         return self.returnmsg
        
    def mainloop(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitgame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.exitgame()
                    if event.key == pygame.K_g:
                        self.returnmsg = "game"
                        self.exitgame() 
                    if event.key == pygame.K_s:
                        self.startgame(False, None)
                    if event.key == pygame.K_c:
                        self.startgame(True, "localhost")
            self.screen.fill((255,255,255))
            pygame.display.update()
            self.clock.tick(30)
            
    def exitgame(self):
        self.quit = True
    def startgame(self, isclient, serverip):
        Game.Game(isclient, serverip, self.screen, self.clock)
    
    
if __name__ == "__main__":
    quit = False
    returnmsg = "main"
    pygame.init()
    screen = pygame.display.set_mode((400,400))
    clock = pygame.time.Clock()
    while not quit:
        if returnmsg == "main":
            returnmsg = PacCatcher(screen, clock)
        elif returnmsg == "game":
            returnmsg = Game.Game(True, screen, clock)
        else:
            quit = True