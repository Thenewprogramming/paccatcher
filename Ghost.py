import pygame
import sys, os


class Ghost(pygame.sprite.Sprite):
    color = None
    score = None
    name = None
    speed = None #Can be boosted when we add potion-like items that appear randomly
    image = None
    
    def __init__(self, color, score, name, speed):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.score = score
        self.name = name
        if not speed == None:
            self.speed = speed
        self.image = pygame.image.load_basic(os.path.join("img", 'Pacman.bmp'))
        self.rect = self.image.get_rect()
    def setcolor(self, color):
        self.color = color
    def update(self):
        pygame.display.get_surface().blit(self.image, (200,200), area=None, special_flags = 0)