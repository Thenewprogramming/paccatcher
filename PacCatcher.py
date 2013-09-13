import pygame
import Game
import inputbox2

"""
This is the mainmenu class of the game.
"""


def init():
    global quitgame
    pygame.display.set_caption("PacCatcher")

    quitgame = False
    name = ""
    ip = ""
    name_input = None
    ip_input = None
    isclient = None

    color_server = color_client = (255, 0, 0)
    serverBtn = pygame.Rect((50, 50), (100, 25))
    clientBtn = pygame.Rect((250, 50), (100, 25))
    startBtn = pygame.Rect((300, 320), (90, 70))

    while not quitgame:

        if name_input != None:
            if name_input.getFocus():
                name, clear_name = name_input.update()
                if clear_name:
                    name_input = None
                    clear_name = False

        if ip_input != None:
            if ip_input.getFocus():
                ip, clear_ip = ip_input.update()
                if clear_ip:
                    ip_input = None
                    clear_ip = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouserect = pygame.Rect(pygame.mouse.get_pos(), (1, 1))
                if mouserect.colliderect(clientBtn):
                    name_input = inputbox2.inputbox(screen, "Your name", [screen.get_width() / 2, 100], (255, 255, 255), (0, 0, 0))
                    ip_input = inputbox2.inputbox(screen, "Servers ip", [screen.get_width() / 2, 200], (255, 255, 255), (0, 0, 0))
                    isclient = True
                elif mouserect.colliderect(serverBtn):
                    name_input = inputbox2.inputbox(screen, "Your name", [screen.get_width() / 2, 100], (255, 255, 255), (0, 0, 0))
                    ip_input = None
                    isclient = False
                elif mouserect.colliderect(startBtn):
                    print("Here we should start the game :P\nInfo: " + str(isclient) + " " + str(ip) + " " + str(name))
                    startgame(isclient, ip, name)
                elif name_input != None:
                    if mouserect.colliderect(name_input.getRect()):
                        name_input.setFocus(True)
                        if isclient and ip_input != None:
                            ip_input.setFocus(False)
                elif ip_input != None:
                    if mouserect.colliderect(ip_input.getRect()):
                        ip_input.setFocus(True)
                        if name_input != None:
                            name_input.setFocus(False)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exitgame()

        screen.fill((255, 255, 255))

        fontobject = pygame.font.Font(None, 30)

        pygame.draw.rect(screen, color_client, clientBtn)
        pygame.draw.rect(screen, color_server, serverBtn)
        pygame.draw.rect(screen, (255, 0, 0), startBtn)
        screen.blit(fontobject.render("server", True, (0, 0, 0)), (60, 55))
        screen.blit(fontobject.render("client", True, (0, 0, 0)), (260, 55))
        screen.blit(fontobject.render("Start", True, (0, 0, 0)), (322, 345))

        if name_input != None:
            name_input.draw()
        if ip_input != None:
            ip_input.draw()

        pygame.display.update()
        clock.tick(30)


def exitgame():
    global quitgame
    quitgame = True


def startgame(isclient, ip, name):
    print("This is the ip: " + ip)
    Game.init(isclient, ip, name, screen, clock)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()
    init()
