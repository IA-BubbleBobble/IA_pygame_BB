import pygame
from tutorial_test.TILE import *

WIDTH = 1050
HEIGHT = 700
fps = 60

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Bobble") #game title

sprit_group = pygame.sprite.Group()

# test grid
# def draw_grid():
#     TILESIZE = 70
#     for x in range(0, WIDTH, TILESIZE):
#         pygame.draw.line(screen, (0,0,0,50), (x, 0), (x,HEIGHT))
#     for y in range(0, HEIGHT, TILESIZE):
#         pygame.draw.line(screen, (0,0,0,50), (0,y), (WIDTH, y))

# 계속 화면이 보이도록 한다
while True:
    screen.fill(BLACK) # clear screen
    # screen.fill(WHITE)
    # draw_grid()

    map_data = []
    #read map_file
    tut_map = "tut_map.txt"
    with open(tut_map, 'r') as file:
        for line in file:
            map_data.append(line.strip('\n').split(' '))

    for col in range(0, len(map_data)):
        for row in range(0, len(map_data[col])):
            print('map_data[col][row]', map_data[col][row])
            if map_data[col][row] == "b":
                tut_big = tut_tile_big(col, row)
                sprit_group.add(tut_big)
            if map_data[col][row] == "t":
                tut_small_top = tut_tile_small_top(col, row)
                sprit_group.add(tut_small_top)
            if map_data[col][row] == "s":
                tut_small_bot = tut_tile_small_bot(col, row)
                sprit_group.add(tut_small_bot)
    sprit_group.draw(screen)

    pygame.display.flip() # 화면 다시 그리기

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x를 눌렀으면
            pygame.quit() #terminate game
            exit() #exit while loop
