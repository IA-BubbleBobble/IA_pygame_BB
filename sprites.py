import os
import pygame
import random
from setting import *

class TutMap(pygame.sprite.Sprite):
    def __init__(self, game, image, col, row):
        self.mapName = mapFile[0]
        self.mapKey = mapTxt[0]
        self.groups = game.all_sprites, game.TutMap
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load("image/"+image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y


class Character(pygame.sprite.Sprite): # character는 단일 객체
    def __init__(self, game):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.initImage = pygame.transform.scale(pygame.image.load("image/charR.png"), (45, 45))
