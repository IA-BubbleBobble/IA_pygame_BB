import os
import pygame
import random
from setting import *
vec = pygame.math.Vector2

class Platform(pygame.sprite.Sprite):
    def __init__(self, image, x, y, w, h): # (x좌표, y좌표, width, height)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/"+image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#
#
# class TutMap(pygame.sprite.Sprite):
#     def __init__(self, game, image, col, row):
#         self.mapName = mapFile[0]
#         self.mapKey = mapTxt[0]
#         self.groups = game.all_sprites, game.tutMap
#         pygame.sprite.Sprite.__init__(self, self.groups)
#         self.grid_x = row * TILESIZE
#         self.grid_y = col * TILESIZE
#         self.image = pygame.image.load("image/"+image).convert_alpha()
#         self.rect = self.image.get_rect()
#         self.rect.x = self.grid_x
#         self.rect.y = self.grid_y

class Player(pygame.sprite.Sprite): # character는 단일 객체
    def __init__(self, game):
        # self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self)
        # self.grid_x = player_pos[0]
        # self.grid_y = player_pos[1]
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load("image/charR.png"), (45, 45)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = player_pos[0]
        self.rect.y = player_pos[1]
        self.pos = vec(player_pos[0], player_pos[1])
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.y += 0.1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 0.1
        if hits:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos[0] = player_pos[0] - 20
            if(player_pos[0]) <= 70:
                player_pos[0] = 70
        if keys[pygame.K_RIGHT]:
            player_pos[0] = player_pos[0] + 20
            if (player_pos[0]) >= 70*14:
                player_pos[0] = 70*14

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x >= WIDTH:
            self.pos.x = WIDTH
        if self.pos.x <= 70:
            self.pos.x = 70

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
