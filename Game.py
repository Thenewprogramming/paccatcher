"""
Needs rewriting
"""

import pygame
import Client
import Server
import threading


def init(client, ip, scree, cloc):
    global isclient, screen, clock, quitgame, keys, serverthread
    isclient = client
    serverip = ip
    screen = scree
    clock = cloc
    quitgame = False
    if isclient:
        Client.SetAdress(serverip, 1234)
    elif not isclient:
        serverthread = threading.Thread(target=Server.startserver, args=(1234,))
        serverthread.start()
    mainloop()


def mainloop():
    global startup, ghosts
    keys = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]

    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                returntomenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    returntomenu()
                if event.key in keys:
                    pass

        screen.fill((0, 0, 0))
        pygame.display.update()
        clock.tick(60)


def returntomenu():
    global quitgame
    quitgame = True
    if isclient:
        pass
    elif not isclient:
        Server.stopserver()

