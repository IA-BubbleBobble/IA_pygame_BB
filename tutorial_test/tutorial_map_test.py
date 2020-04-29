# 1. pygame module 불러오기
import pygame

# 2. pygame initialize
pygame.init()
width, height = 1100, 700 # width, height init
screen = pygame.display.set_mode((width, height)) # width, height넣어서 screen이라는 객체 생성

# 3. 이미지를 가져온다
map_tut_big = pygame.transform.scale(pygame.image.load("image/map_tutorial_1(big).PNG"), (70, 70)) # 이 image를 가지고 객체를 만들겠다
map_tut_small = pygame.transform.scale(pygame.image.load("image/map_tutorial_2(small).PNG"), (70, 20))
keys = [False, False, False, False, False] # key를 눌렀는지 안눌렀는지
player_pos = [100, 100] # player의 위치 좌표(움직일 때마다 변경해야하니까 리스트로)

# 4. 계속 화면이 보이도록 한다
while True:
    # 5. clear screen
    screen.fill((0,0,0)) #(R,G,B)

    # 6. 모든 요소들을 다시그린다(풀위에 player-> 풀을 먼저 그린 후 player그린다)
    # print("small",map_tut_small.get_width()) #116
    # print(map_tut_big.get_width()) #76
    # print("small", map_tut_small.get_height()) #23
    # print(map_tut_big.get_height()) #73

    for x in range(width//map_tut_small.get_width() + 1):
        screen.blit(map_tut_small, (x*70, 50))
        screen.blit(map_tut_small, (x*70, 630))
    for y in range(height // map_tut_big.get_height() - 2):
        screen.blit(map_tut_big, (0, (y+1)*70))
        screen.blit(map_tut_big, (1030, (y+1)*70))

    screen.blit(map_tut_small, (210, 490))
    for i in range(10):
        screen.blit(map_tut_small, (70*(3+i), 420))
    screen.blit(map_tut_small, (820, 210))
#-----------------------------------------------------------------------------------------------------
    # 7. 화면을 다시 그린다.
    pygame.display.flip()

    # 8. 게임을 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x를 눌렀으면
            pygame.quit() #terminate game
            exit() #exit while loop
        if event.type == pygame.KEYDOWN: # key가 눌려지는 type의 event이면
            if event.key == pygame.K_w: # w키가 눌려지면
                keys[0] = True
            elif event.key == pygame.K_a: # a키가 눌려지면
                keys[1] = True
            if event.key == pygame.K_s: # s키가 눌려지면
                keys[2] = True
            if event.key == pygame.K_d: # d키가 눌려지면
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: # w키를 떼면
                keys[0] = False
            elif event.key == pygame.K_a: # a키를 떼면
                keys[1] = False
            if event.key == pygame.K_s: # s키를 떼면
                keys[2] = False
            if event.key == pygame.K_d: # d키를 떼면
                keys[3] = False

    #9 Move player
    if keys[0]:
        print(player_pos)
        player_pos[1] = player_pos[1] - 5 # y값 감소 -> 위로이동
        if(player_pos[1] < 0):
            player_pos[1] = 0
    elif keys[2]:
        print(player_pos)
        player_pos[1] = player_pos[1] + 5 # y값 증가 -> 아래로 이동
        if(player_pos[1] > 480):
            player_pos[1] = 480
    if keys[1]:
        print(player_pos)
        player_pos[0] = player_pos[0] - 5 # x값 감소 -> 왼쪽으로 이동
        if (player_pos[0] < 100):
            player_pos[0] = 100
    elif keys[3]:
        print(player_pos)
        player_pos[0] = player_pos[0] + 5 # x값 증가 -> 오른쪽으로 이동
        if (player_pos[0] > 640):
            player_pos[0] = 640