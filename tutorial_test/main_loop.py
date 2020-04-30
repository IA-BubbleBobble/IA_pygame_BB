# 1. pygame module 불러오기
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

# keys = [False, False, False, False, False] # key를 눌렀는지 안눌렀는지
# player_pos = [100, 100] # player의 위치 좌표(움직일 때마다 변경해야하니까 리스트로)
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
#-----------------------------------------------------------------------------------------------------
    # 7. 화면을 다시 그린다.
    pygame.display.flip()

    # 8. 게임을 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x를 눌렀으면
            pygame.quit() #terminate game
            exit() #exit while loop
    #     if event.type == pygame.KEYDOWN: # key가 눌려지는 type의 event이면
    #         if event.key == pygame.K_w: # w키가 눌려지면
    #             keys[0] = True
    #         elif event.key == pygame.K_a: # a키가 눌려지면
    #             keys[1] = True
    #         if event.key == pygame.K_s: # s키가 눌려지면
    #             keys[2] = True
    #         if event.key == pygame.K_d: # d키가 눌려지면
    #             keys[3] = True
    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_w: # w키를 떼면
    #             keys[0] = False
    #         elif event.key == pygame.K_a: # a키를 떼면
    #             keys[1] = False
    #         if event.key == pygame.K_s: # s키를 떼면
    #             keys[2] = False
    #         if event.key == pygame.K_d: # d키를 떼면
    #             keys[3] = False
    #
    # #9 Move player
    # if keys[0]:
    #     print(player_pos)
    #     player_pos[1] = player_pos[1] - 5 # y값 감소 -> 위로이동
    #     if(player_pos[1] < 0):
    #         player_pos[1] = 0
    # elif keys[2]:
    #     print(player_pos)
    #     player_pos[1] = player_pos[1] + 5 # y값 증가 -> 아래로 이동
    #     if(player_pos[1] > 480):
    #         player_pos[1] = 480
    # if keys[1]:
    #     print(player_pos)
    #     player_pos[0] = player_pos[0] - 5 # x값 감소 -> 왼쪽으로 이동
    #     if (player_pos[0] < 100):
    #         player_pos[0] = 100
    # elif keys[3]:
    #     print(player_pos)
    #     player_pos[0] = player_pos[0] + 5 # x값 증가 -> 오른쪽으로 이동
    #     if (player_pos[0] > 640):
    #         player_pos[0] = 640