import pygame
import os


class Ghost(pygame.sprite.Sprite):
    color = None
    score = None
    name = None
    speed = None #Can be boosted when we add potion-like items that appear randomly
    image = None
    whichimage = 1

    def __init__(self, color, score, name, speed):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.score = score
        self.name = name
        if not speed == None:
            self.speed = speed
        self.image = pygame.image.load(os.path.join("img", 'pcman1.png'))
        self.rect = self.image.get_rect()

    def setcolor(self, color):
        self.color = color

    def update(self):
        if (self.whichimage == 1):
            self.image = pygame.image.load(os.path.join("img", 'pcman1.png'))
        if (self.whichimage == 2):
            self.image = pygame.image.load(os.path.join("img", 'pcman2.png'))
        if (self.whichimage == 3):
            self.image = pygame.image.load(os.path.join("img", 'pcman3.png'))    
        if (self.whichimage == 4):
            self.image = pygame.image.load(os.path.join("img", 'pcman4.png'))
        if (self.whichimage == 5):
            self.image = pygame.image.load(os.path.join("img", 'pcman5.png'))
        
        pygame.display.get_surface().blit(self.image, (200,200), area=None, special_flags = 0)
        
        if (self.whichimage < 5):
            self.whichimage += 1
        else:
            self.whichimage = 1
        