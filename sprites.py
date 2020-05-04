import os
import pygame
import random
from setting import *
vec = pygame.math.Vector2
import time

class Player(pygame.sprite.Sprite): # character는 단일 객체
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.imageLNum = 0
        self.imageRNum = 0
        self.imageLoad = charR[self.imageRNum]
        self.image = pygame.transform.scale(pygame.image.load(self.imageLoad), (45, 45)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = 620
        self.pos = vec(player_pos[0], player_pos[1])
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

class Monster (pygame.sprite.Sprite):
    def __init__(self, game, location, direction, state): # 맵마다 나타나는 몬스터의 위치가 달라 location이라는 변수를 넣어주었다.
        pygame.sprite.Sprite.__init__(self)
        self.game = game 
        self.groups = game.all_sprites, game.platforms
        # 몬스터의 상태가 bubble인지 확인한다
        # 아마 몬스터가 버블에 닿아서 안으로 들어가면 True가 될 예정
        self.monstar_bubble = False
        #몬스터가 죽은 상태 인지 확인한다
        self.monstar_dead = False
        self.location = location
        # 몬스터가 처음 맵에 나타날 때 보는 방향에 따라 다른 이미지를 불러준다.
        self.direction = direction
        #현재 몬스터의 상태가 살아있으면 live, bubble상태면 bubble, 죽은 상태면 dead
        self.state = state
        # 몬스터가 죽을 때 속도를 늦춰주기 위해 사용하는 변수
        self.slow = 0
        self.updown = 0
        if(self.state == 'live'):
            if(self.direction == 'left'):
                self.image = pygame.transform.scale(pygame.image.load(monstarLD), (45, 45)).convert_alpha()
            elif(self.direction == 'right'):
                self.image = pygame.transform.scale(pygame.image.load(monstarRD), (45, 45)).convert_alpha()
        elif(self.state == 'dead'):
            if(self.direction == 'left'):
                self.image = pygame.transform.scale(pygame.image.load(monstarDL1), (45, 45)).convert_alpha()
            elif(self.direction == 'right'):
                self.image = pygame.transform.scale(pygame.image.load(monstarDR1), (45, 45)).convert_alpha()
        self.updown += 1
        self.rect = self.image.get_rect()
        self.pos = vec(self.location)
        self.rect.x = location[0]
        self.rect.y = location[1]
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        
    def update(self):
        if(self.state == 'live'):
            self.acc = vec(0, PLAYER_GRAVITY)
            if(self.direction == 'left') :
                self.acc.x = - MONSTAR_ACC
            elif(self.direction == 'right'):
                self.acc.x = MONSTAR_ACC
            
            if(self.direction == 'left'):
                if(self.updown % 2 == 0) :
                    self.image = pygame.transform.scale(pygame.image.load(monstarLD), (45, 45)).convert_alpha()
                else:
                    self.image = pygame.transform.scale(pygame.image.load(monstarLU), (45, 45)).convert_alpha()
            else :
                if(self.updown%2== 0) :
                    self.image = pygame.transform.scale(pygame.image.load(monstarRD), (45, 45)).convert_alpha()
                else:
                    self.image = pygame.transform.scale(pygame.image.load(monstarRU), (45, 45)).convert_alpha()
            self.updown += 1

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

        elif (self.state == 'dead'):
            if(self.slow %3 == 0) :
                if(self.direction == 'left'):
                    if(self.updown % 4 == 1) :
                        self.image = pygame.transform.scale(pygame.image.load(monstarDL1), (45, 45)).convert_alpha()
                    elif(self.updown % 4 ==2):
                        self.image = pygame.transform.scale(pygame.image.load(monstarDL2), (45, 45)).convert_alpha()
                    elif (self.updown % 4 ==3):
                        self.image = pygame.transform.scale(pygame.image.load(monstarDL3), (45, 45)).convert_alpha()
                    else:
                        self.image = pygame.transform.scale(pygame.image.load(monstarDL4), (45, 45)).convert_alpha()
                else :
                    if(self.updown % 4 == 1) :
                        self.image = pygame.transform.scale(pygame.image.load(monstarDR1), (45, 45)).convert_alpha()
                    elif(self.updown % 4 ==2):
                        self.image = pygame.transform.scale(pygame.image.load(monstarDR2), (45, 45)).convert_alpha()
                    elif (self.updown % 4 ==3):
                        self.image = pygame.transform.scale(pygame.image.load(monstarDR3), (45, 45)).convert_alpha()
                    else:
                        self.image = pygame.transform.scale(pygame.image.load(monstarDR4), (45, 45)).convert_alpha()

                self.updown += 1
                if(self.direction == 'left') :
                    self.acc.x = - (MONSTAR_ACC+ 0.8)
                elif(self.direction == 'right'):
                    self.acc.x = (MONSTAR_ACC+0.8)   
                    
                self.acc.x += self.vel.x * MONSTAR_FRICTION
                self.vel += self.acc
                self.pos += self.vel + 0.5 * self.acc
            
                if self.pos.x >= WIDTH-140:
                    self.pos.x = WIDTH-140
                elif self.pos.x <= 70:
                    self.pos.x = 70

                if self.pos.y >= HEIGHT-68 :
                    self.pos.y -= 50
                elif (self.pos.y <= 150):
                    self.pos.y == 150
                else : 
                    self.pos.y -= 50

                hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
                if hits:
                    print("hits!============================")
                    self.pos.y = hits[0].rect.y-45
                    self.vel.y = 0
                        
                self.rect.x = self.pos.x
                self.rect.y = self.pos.y

                if(self.updown > 6):
                    print('monstar kill')
                    self.kill()
            self.slow += 1
        else:
            pass
            # monstar가 버블 상태이지만 죽지는 않았을 때
        self.mask = pygame.mask.from_surface(self.image)

class Item(pygame.sprite.Sprite): # character는 단일 객체
    def __init__(self, game,image,location): 
        pygame.sprite.Sprite.__init__(self)
        self.game = game 
        self.groups = game.all_sprites, game.platforms
        self.location = location
        self.count = 0 # 몬스터가 사라진 후에 나오기 위해서 21번 이상 돈 이후부터 나타나기 위핸 사용되는 변수
        self.type = image # 나중에 image이름으로 점수를 더하기 위해 사용되는 변수
        self.item_image = item_dic[image]
        self.image = pygame.transform.scale(pygame.image.load(EMPTY), (45, 45)).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = vec(self.location)
        self.rect.x = self.location[0]
        self.rect.y = self.location[1]
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.hit = False # item이 내려 오다가 충돌하면 움직이지 않게 하기 위해서

    def update(self):
        if(self.count > 21):
            if(not self.hit) :
                self.image = pygame.transform.scale(pygame.image.load(self.item_image), (45, 45)).convert_alpha()
                if self.pos.y >= HEIGHT-68 :
                    self.pos.y = HEIGHT-68
                elif self.pos.y <= 150:
                    self.pos.y = 150
                else:
                    self.pos.y +=50
                
                hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
                if hits:
                    print("hits!============================")
                    self.pos.y = hits[0].rect.y-45 + 0.1 # 벽돌위로
                    self.vel.y = 0
                    self.hit = True
            plus = random.choice([i for i in range(0,40,5)])
            if(self.count == 22):
                self.rect.x = self.pos.x + plus
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
        self.count += 1

