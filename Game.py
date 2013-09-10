import pygame
import Client


def init(isclient, serverip, name, screen, clock):

    screen.fill((0, 0, 0))
    pygame.display.update()

    if isclient:
        try:
            host, port = serverip.split(":")
        except ValueError:
            host = serverip
            port = 1234
        Client.connect(host, port)
        Client.ready(name)
        
    else:
        pass