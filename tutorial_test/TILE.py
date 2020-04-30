import pygame
from os import path

WIDTH = 1100
HEIGHT = 700
fps = 60
#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TILESIZE = 70

class tut_tile_big(pygame.sprite.Sprite) :
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load("image/tutMapBig.PNG").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

class tut_tile_small_top(pygame.sprite.Sprite):
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load("image/tutMapStop.PNG").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

class tut_tile_small_bot(pygame.sprite.Sprite):
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load("image/tutMapSbot.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y