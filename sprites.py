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
        self.pos = vec(player_pos[0]+20, player_pos[1]+20)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.y += 0.1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 0.1
        if hits:
            print("hits!===============")
            self.vel.y = -17.5 # 점프 높이

    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x >= WIDTH-140:
            self.pos.x = WIDTH-140
        elif self.pos.x <= 70:
            self.pos.x = 70
        if self.pos.y >= HEIGHT-68:
            self.pos.y = HEIGHT-68
        elif self.pos.y <= 150:
            self.pos.y = 150


        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

class Monstar (pygame.sprite.Sprite):
    def __init__(self, game,location,direction): # 맵마다 나타나는 몬스터의 위치가 달라 location이라는 변수를 넣어주었다.
        pygame.sprite.Sprite.__init__(self)
        self.game = game 
        self.groups = game.all_sprites, game.platforms
        self.location = location
        # 몬스터가 처음 맵에 나타날 때 보는 방향에 따라 다른 이미지를 불러준다.
        self.direction = direction
        self.updown = 0
        if(self.direction == 'left'):
            self.image = pygame.transform.scale(pygame.image.load(monstarLD), (45, 45)).convert_alpha()
        elif(self.direction == 'right'):
            self.image = pygame.transform.scale(pygame.image.load(monstarRD), (45, 45)).convert_alpha()
        self.updown += 1
        self.rect = self.image.get_rect()
        self.pos = vec(self.location)
        self.rect.x = location[0]
        self.rect.y = location[1]
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        
    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        if(self.direction == 'left') :
            self.acc.x = - MONSTAR_ACC
        elif(self.direction == 'right'):
            self.acc.x = MONSTAR_ACC
        
        if(self.direction == 'left'):
            if(self.updown == 0) :
                self.image = pygame.transform.scale(pygame.image.load(monstarLD), (45, 45)).convert_alpha()
                self.updown = 1
            else:
                self.image = pygame.transform.scale(pygame.image.load(monstarLU), (45, 45)).convert_alpha()
                self.updown = 0
        else :
            if(self.updown == 0) :
                self.image = pygame.transform.scale(pygame.image.load(monstarRD), (45, 45)).convert_alpha()
                self.updown = 1
            else:
                self.image = pygame.transform.scale(pygame.image.load(monstarRU), (45, 45)).convert_alpha()
                self.updown = 0

        self.acc.x += self.vel.x * MONSTAR_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
   
        if self.pos.x >= WIDTH-140:
            self.pos.x = WIDTH-140
            self.direction = 'left'
        elif self.pos.x <= 70:
            self.pos.x = 70
            self.direction = 'right'

        if self.pos.y >= HEIGHT-68 :
            self.pos.y = HEIGHT-68
        elif self.pos.y <= 150:
            self.pos.y = 150

        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        if hits:
            print("hits!============================")
            self.pos.y = hits[0].rect.y-45 + 0.1 # 벽돌위로
            self.vel.y = 0
            
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y