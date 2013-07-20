import pygame
import os


class Ghost(pygame.sprite.Sprite):
    color = None
    score = None
    name = None
    speed = None  # Can be boosted when we add potion-like items that appear randomly
    image = None
    whichimage = 1

    def __init__(self, color, score, name, speed):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.score = score
        self.name = name
        self.pos = (200, 200)
        if not speed == None:
            self.speed = speed

        self.image = pygame.image.load(os.path.join("img", 'pcman1.png'))
        self.rect = self.image.get_rect()

        print (self.rect)

    def setcolor(self, color):
        self.color = color

    def getpos(self):
        return self.pos

    def update(self, pos):
        pos = (int(pos[0]), int(pos[1]))

        if self.whichimage < 2:
            self.image = pygame.image.load(os.path.join("img", 'pcman1.png'))
        elif self.whichimage < 10:
            self.image = pygame.image.load(os.path.join("img", 'pcman' + str(int(self.whichimage / 2)) + '.png'))
        elif self.whichimage > 10:
            self.image = pygame.image.load(os.path.join("img", 'pcman' + str(int((self.whichimage - 8) / 2)) + '.png'))

        if (self.whichimage < 18):
            self.whichimage += 1
        else:
            self.whichimage = 1
