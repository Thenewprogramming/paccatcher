import pygame
import Server
import threading
import Client
# from pygame.locals import *

class PacCatcher():
    
    def __init__(self):
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((400,400))
        self.quit = False
        self.isclient = True
        if self.isclient:
            Client.SetAdress("localhost", 1234)
            #Client.SendMessage("Alive!")
        elif not self.isclient:
            self.server = threading.Thread(target=Server.startserver)
            self.server.start()
        self.mainloop()
    
    def mainloop(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitgame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.exitgame()        
            self.screen.fill((255,255,255))
            pygame.display.update()
            self.fpsClock.tick(30)
            
    def exitgame(self):
        #close socket and eventually save files
        if self.isclient:
            pass
        elif self.isserver:
            Server.stopserver()
        self.quit = True

if __name__ == "__main__":
    PacCatcher()
    
        