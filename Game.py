import pygame
import Client
import Server
import PacCatcher
import threading

class Game():
    
    def __init__(self, isclient, serverip, screen, clock):
        self.isclient = isclient
        self.screen = screen
        self.clock = clock
        self.quit = False
        self.returnmsg = ""
        if isclient:
            Client.SetAdress(serverip, 1234)
        elif not isclient:
            self.serverthread = threading.Thread(target=Server.startserver(1234))
            self.serverthread.start()
        self.mainloop()
        
    def mainloop(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.returntomenu()
            self.screen.fill((0,0,0))
            pygame.display.update()
            self.clock.tick(30)
            
    def returntomenu(self):
        self.quit = True
        self.returnmsg = "main"
        if self.isclient:
            pass
        elif not self.isclient:
            Server.stopserver()
        
if __name__ == "__main__":
    Game(True)