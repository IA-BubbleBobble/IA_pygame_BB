import os
import pygame
import random
from setting import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite): # character는 단일 객체
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.imageLNum = 0
        self.imageRNum = 0
        self.imageLoad = charR[self.imageRNum]
        self.image = pygame.transform.scale(pygame.image.load(self.imageLoad), (45, 45)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = player_pos[0]
        self.rect.y = player_pos[1]
        self.pos = vec(player_pos[0]+20, player_pos[1]+20)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        print("class Player jump fucntion")
        # jump only if standing on a platform
        self.rect.y += 0.1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 0.1
        if hits:
            print("hits!===============")
            self.vel.y = -15.5 # 점프 높이

    def update(self):
        print("class Player update function")
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.game.lr = 0
            self.imageLoad = charL[self.imageLNum]
            self.imageLNum += 1
            if (self.imageLNum >= 3):
                self.imageLNum = 0
            self.image = pygame.transform.scale(pygame.image.load(self.imageLoad), (45, 45)).convert_alpha()
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.game.lr = 1
            self.imageLoad = charR[self.imageRNum]
            self.imageRNum += 1
            if (self.imageRNum >= 3):
                self.imageRNum = 0
            self.image = pygame.transform.scale(pygame.image.load(self.imageLoad), (45, 45)).convert_alpha()
            self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x >= WIDTH-130:
            self.pos.x = WIDTH-130
        elif self.pos.x <= 70:
            self.pos.x = 70
        if self.pos.y >= HEIGHT-68:
            self.pos.y = HEIGHT-68
        elif self.pos.y <= 150:
            self.pos.y = 150


        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

class Platform(pygame.sprite.Sprite):
    def __init__(self, image, x, y, w, h): # (x좌표, y좌표, width, height)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bubble(pygame.sprite.Sprite):
    def __init__(self, game, image, lr, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.imageLoad = image
        self.image = pygame.transform.scale(pygame.image.load(image), (35, 35)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tempXL = x - 300
        self.tempXR = x + 300
        self.speedyR = 10
        self.speedyL = -10
        self.lr = lr

    def update(self):
        if(self.lr == 0): # left
            self.rect.x += self.speedyL
            if self.rect.x <= self.tempXL:
                self.kill()
            if self.rect.x <= 70:
                self.kill()
        elif(self.lr == 1): # right
            self.rect.x += self.speedyR
            if self.rect.x >= self.tempXR:
                self.kill()
            if self.rect.x >= WIDTH - 140:
                self.kill()
        # if(self.imageLoad == bubble1):
        #     self.tempXL = self.rect.x - 70
        #     self.tempXR = self.rect.x + 70
        #     print("tempXL:", self.tempXL)
        #     if(self.lr == 0): # plyaer가 왼쪽 보고있을 때
        #         self.rect.x += self.speedyL
        #         if self.rect.x < self.tempXL:
        #             self.kill()
        #         if self.rect.x <= 70:
        #             self.kill()
        #     elif(self.lr == 1): #player가 오른쪽 보고있을 때
        #         self.rect.x += self.speedyR
        #         if self.rect.x >= self.tempXR:
        #             self.kill()
        #         if self.rect.x >= WIDTH - 70:
        #             self.kill()
        #
        # elif (self.imageLoad == bubble2):
        #     self.rect.x += 70
        #     self.tempXL = self.rect.x - 140
        #     self.tempXR += self.rect.x + 140
        #     print("tempXL:", self.tempXL)
        #     if (self.lr == 0):  # plyaer가 왼쪽 보고있을 때
        #         self.rect.x += self.speedyL
        #         if self.rect.x < self.tempXL:
        #             self.kill()
        #         if self.rect.x <= 70:
        #             self.kill()
        #     elif (self.lr == 1):  # player가 오른쪽 보고있을 때
        #         self.rect.x += self.speedyR
        #         if self.rect.x >= self.tempXR:
        #             self.kill()
        #         if self.rect.x >= WIDTH - 70:
        #             self.kill()
        #
        # elif (self.imageLoad == bubble3):
        #     self.rect.x += 140
        #     self.tempXL = self.rect.x - 210
        #     self.tempXR = self.rect.x + 210
        #     print("tempXL:", self.tempXL)
        #     if (self.lr == 0):  # plyaer가 왼쪽 보고있을 때
        #         self.rect.x += self.speedyL
        #         if self.rect.x < self.tempXL:
        #             self.kill()
        #         if self.rect.x <= 70:
        #             self.kill()
        #     elif (self.lr == 1):  # player가 오른쪽 보고있을 때
        #         self.rect.x += self.speedyR
        #         if self.rect.x >= self.tempXR:
        #             self.kill()
        #         if self.rect.x >= WIDTH - 70:
        #             self.kill()
        #
        # elif (self.imageLoad == bubble4):
        #     self.rect.x += 210
        #     self.tempXL = self.rect.x - 280
        #     self.tempXR = self.rect.x + 280
        #     if (self.lr == 0):  # plyaer가 왼쪽 보고있을 때
        #         self.rect.x += self.speedyL
        #         if self.rect.x < self.tempXL:
        #             self.kill()
        #         if self.rect.x <= 70:
        #             self.kill()
        #     elif (self.lr == 1):  # player가 오른쪽 보고있을 때
        #         self.rect.x += self.speedyR
        #         if self.rect.x >= self.tempXR:
        #             self.kill()
        #         if self.rect.x >= WIDTH - 70:
        #             self.kill()