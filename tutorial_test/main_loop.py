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
#(qaz), (wsx), (edc), (rfv) : map tile(big, small_top, small_bottom)

map = ["tut_map.txt", "stage1_map.txt"]
mapTxt = [("q", "a", "z"), ("q", "a", "z")] # (big, small_top, small_bottom, shadow)
mapImage = [("tutMapBig", "tutMapStop", "tutMapSbot"), ("s1MapBig", "s1MapStop", "s1MapSbot")] # (big, small_top, small_bottom)

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

    #change index == change stage map
    map_data = []
    map_name = map[0] #tutorial map
    with open(map_name, 'r') as file:
        for line in file:
            map_data.append(line.strip('\n').split(' '))

    for col in range(0, len(map_data)): #세로
        for row in range(0, len(map_data[col])): #가로
            if map_data[col][row] == mapTxt[0][0]:
                map_big = Map(mapImage[0][0], col, row)
                sprit_group.add(map_big)
            if map_data[col][row] == mapTxt[0][1]:
                map_small_top = Map(mapImage[0][1], col, row)
                sprit_group.add(map_small_top)
            if map_data[col][row] == mapTxt[0][2]:
                map_small_bot = Map(mapImage[0][2], col, row)
                sprit_group.add(map_small_bot)
            # shadow 넣는거 추가
    sprit_group.draw(screen)

    pygame.display.flip() # 화면 다시 그리기

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x를 눌렀으면
            pygame.quit() #terminate game
            exit() #exit while loop
