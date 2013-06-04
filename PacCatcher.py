import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        print('hoi')
        
    pygame.display.update()
    fpsClock.tick(30)