import pygame
import Client
import Server
import PacCatcher

class Game():
    
    def __init__(self, isclient, screen, clock):
        self.screen = screen
        self.clock = clock
        self.quit = False
        self.returnmsg = ""
        if isclient:
            Client.SetAdress("localhost", 1234)
        elif not isclient:
            self.server = threading.Thread(target=Server.startserver)
            self.server.start()
        self.mainloop()
        
    def mainloop(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.returntomenu()
            self.screen.fill((0,0,0))
            self.screen.update()
            self.clock.tick(30)
            
    def returntomenu(self):
        self.quit = True
        self.returnmsg = "main"
        if self.isclient:
            pass
        elif self.isserver:
            Server.stopserver()
        
if __name__ == "__main__":
    Game(True)