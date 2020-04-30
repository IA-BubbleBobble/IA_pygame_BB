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
mapImage = [("tutMapBig", "tutMapStop", "tutMapS"), ("s1MapBig", "s1MapStop", "s1MapSbot")] # (big, small_top, small_bottom)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Bobble") #game title

sprit_group = pygame.sprite.Group()
keys = [False, False, False, False, False] # key를 눌렀는지 안눌렀는지
char_pos = [70, 630] # player의 위치 좌표(움직일 때마다 변경해야하니까 리스트로)
charR = pygame.transform.scale(pygame.image.load("image/charR.png"), (45, 45))
charL = pygame.transform.scale(pygame.image.load("image/charL.png"), (45, 45))
character = charR
# test grid
# def draw_grid():
#     TILESIZE = 70
#     for x in range(0, WIDTH, TILESIZE):
#         pygame.draw.line(screen, (0,0,0,50), (x, 0), (x,HEIGHT))
#     for y in range(0, HEIGHT, TILESIZE):
#         pygame.draw.line(screen, (0,0,0,50), (0,y), (WIDTH, y))

def get_keys(char):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        return charL
    if keys[pygame.K_RIGHT]:
        return charR
    else:
        return char

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
            if(col == len(map_data)-1):
                print("col:",col)
                if map_data[col][row] == mapTxt[0][0]:
                    map_big = Map(mapImage[0][0], col, row)
                    sprit_group.add(map_big)
                if map_data[col][row] == mapTxt[0][1]:
                    map_small_top = Map(mapImage[0][1], col, row)
                    sprit_group.add(map_small_top)
                if map_data[col][row] == mapTxt[0][2]:
                    map_small_bot = Map(mapImage[0][2], 9.65, row)
                    sprit_group.add(map_small_bot)
            else:
                if map_data[col][row] == mapTxt[0][0]:
                    map_big = Map(mapImage[0][0], col, row)
                    sprit_group.add(map_big)
                if map_data[col][row] == mapTxt[0][1]:
                    map_small_top = Map(mapImage[0][1], col, row)
                    sprit_group.add(map_small_top)
                if map_data[col][row] == mapTxt[0][2]:
                    map_small_bot = Map(mapImage[0][2], col, row)
                    sprit_group.add(map_small_bot)

    sprit_group.draw(screen)
    character = get_keys(character)
    # sprit_group.add(character)
    print("char pos:", char_pos)
    screen.blit(character, char_pos)

    pygame.display.flip() # 화면 다시 그리기

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x를 눌렀으면
            pygame.quit() #terminate game
            exit() #exit while loop
        if event.type == pygame.KEYDOWN:  # key가 눌려지는 type의 event이면
            if event.key == pygame.K_UP:  # 위쪽 방향키가 눌려지면
                keys[0] = True
            elif event.key == pygame.K_LEFT:  # 왼쪽 방향키가 눌려지면
                keys[1] = True
            if event.key == pygame.K_DOWN:  # 아래쪽 방향키가 눌려지면
                keys[2] = True
            if event.key == pygame.K_RIGHT:  # 오른쪽 방향키가 눌려지면
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:  # 위쪽 방향키를 떼면
                keys[0] = False
            elif event.key == pygame.K_LEFT:  # 왼쪽 방향키를 떼면
                keys[1] = False
            if event.key == pygame.K_DOWN:  # 아래쪽 방향키를 떼면
                keys[2] = False
            if event.key == pygame.K_RIGHT:  # 오른쪽 방향키를 떼면
                keys[3] = False

    #9 Move player
    if keys[0]:
        char_pos[1] = char_pos[1] - 20 # y값 감소 -> 위로이동
    elif keys[2]:
        char_pos[1] = char_pos[1] + 20 # y값 증가 -> 아래로 이동
    if keys[1]:
        char_pos[0] = char_pos[0] - 20 # x값 감소 -> 왼쪽으로 이동
    elif keys[3]:
        char_pos[0] = char_pos[0] + 20 # x값 증가 -> 오른쪽으로 이동
