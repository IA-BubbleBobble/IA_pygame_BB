import pygame

TILESIZE = 70
#CHARSIZE = 45

class Map(pygame.sprite.Sprite):
    def __init__(self, image_name, col, row):
        pygame.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        temp_image = "image/"+image_name+".PNG"
        self.image = pygame.image.load(temp_image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
