import pygame
import Client
from Server import server


def init(isclient, serverip, name, screen, clock):

    screen.fill((0, 0, 0))
    pygame.display.update()

    if isclient:
        try:
            host, port = serverip.split(":")
        except ValueError:
            host = serverip
            port = 12341
        Client.connect(host)
        Client.ready(name)

    else:
        try:
            host, port = serverip.split(":")
        except ValueError:
            host = ""
            port = 12341
        Server = server()

    while True:
        if not isclient:
            if Server.isdone():
                break
    for thing in Server.connected:
        print(thing.name)
