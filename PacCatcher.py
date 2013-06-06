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
        self.isserver = True
        self.isclient = True
        if self.isserver:
            self.server = threading.Thread(target=Server.startserver)
            self.server.start()
        elif self.isclient:
            self.client = threading.Thread(target=Client.ConnectToServer, args=("10.16.128.67"))
            
        self.mainloop()
        
        
    def mainloop(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitgame()
                    if self.isserver:
                        Server.stopserver()
                    elif self.isclient:
                        Client.CloseConnection()
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.exitgame()
                        if self.isserver:
                            Server.stopserver()
                        elif self.isclient:
                            Client.CloseConnection()
                        
            self.screen.fill((255,255,255))
            pygame.display.update()
            self.fpsClock.tick(30)
            
    def exitgame(self):
        #close socket and eventually save files
        self.quit = True

if __name__ == "__main__":
    PacCatcher()
    
        