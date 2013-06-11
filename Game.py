import pygame
import Client
import Server
import Ghost
import threading


class Game():

    def __init__(self, isclient, serverip, screen, clock):
        self.isclient = isclient
        self.screen = screen
        self.clock = clock
        self.quit = False
        
        if isclient:
            Client.SetAdress(serverip, 1234)
        elif not isclient:
            self.serverthread = threading.Thread(target=Server.startserver, args=(1234,))
            self.serverthread.start()
        self.mainloop()

    def mainloop(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.returntomenu()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.returntomenu()
            self.screen.fill((0, 0, 0))

            self.ghost1 = Ghost.Ghost("red", 0, "ghost 1", 1)
            self.ghost1.update()

            pygame.display.update()
            self.clock.tick(30)

    def returntomenu(self):
        self.quit = True
        if self.isclient:
            pass
        elif not self.isclient:
            Server.stopserver()

    def getplayerpositions(self):
        ghost1 = None
        ghost2 = None
        ghost3 = None
        ghost4 = None
        pacman = None
        
        if (self.isclient):
            pass
        
        return (ghost1, ghost2, ghost3, ghost4, pacman)

if __name__ == "__main__":
    Game(True)
