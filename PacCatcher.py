import pygame
import Server
import SocketServer
import threading
# from pygame.locals import *

class PacCatcher():
    
    
    def __init__(self):
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1366,768), pygame.FULLSCREEN)
        self.quit = False
        self.serverthread = threading.Thread(target=Server.Server, args=(2345))
        #self.serverthread.start()
        self.mainloop()
        
        
    def mainloop(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitgame()
                    Server.Server.StopGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.exitgame()
                        Server.Server.StopGame()
            self.screen.fill((255,255,255))
            pygame.display.update()
            self.fpsClock.tick(30)
            
    def exitgame(self):
        #close socket and eventually save files
        self.quit = True

if __name__ == "__main__":
    PacCatcher()
    
        