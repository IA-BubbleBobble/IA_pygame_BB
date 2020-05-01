import pygame
from setting import *
from sprites import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init() # to use music
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # screen 크기 지정
        pygame.display.set_caption(TITLE) # 게임 창 제목표시줄에 쓰여질 문구
        self.clock = pygame.time.Clock() # 객체를 사용하여 이후 초당 프레임 설정 시 사용
        self.running = True #게임이 끝난지 아닌지 판단 위한 변수
        # self.character = pygame.transform.scale(pygame.image.load("image/charR.png"), (45, 45))

    def new(self): #game start
        # sprite group
        self.all_sprites = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group() # monster sprite group 생성
        self.TutMap = pygame.sprite.Group() #map sprite group 생성
        self.character = Character(self) # self.character, Character 객체 생성
        self.start_tick = pygame.time.get_ticks()

    def run(self): #게임 갱신
        print("run function")
        # game loop
        # back ground music 설정도 여기서
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.screen.blit(self.character.initImage, char_pos)
            self.events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.wait_for_keys()

    def update(self):
        self.all_sprites.update()
        self.TutMap.update()
        # tutorial map 일 때(조건문 추가!!!)
        map_data = []
        with open(mapFile[0], 'r') as file:
            for line in file:
                map_data.append(line.strip('\n').split(' '))

        for col in range(0, len(map_data)):  # 세로
            for row in range(0, len(map_data[col])):  # 가로
                print("map_data[col][row]", map_data[col][row])
                if (col == len(map_data) - 1):
                    print("col:", col)
                    if map_data[col][row] == mapTxt[0][0]:
                        map_big = TutMap(self, tutMapBig, col, row)
                        self.TutMap.add(map_big)
                    if map_data[col][row] == mapTxt[0][1]:
                        map_small_top = TutMap(self, tutMapStop, col, row)
                        self.TutMap.add(map_small_top)
                    if map_data[col][row] == mapTxt[0][2]:
                        map_small_bot = TutMap(self, tutMapS, 9.65, row)
                        self.TutMap.add(map_small_bot)
                else:
                    if map_data[col][row] == mapTxt[0][0]:
                        map_big = TutMap(self, tutMapBig, col, row)
                        self.TutMap.add(map_big)
                    if map_data[col][row] == mapTxt[0][1]:
                        map_small_top = TutMap(self, tutMapStop, col, row)
                        self.TutMap.add(map_small_top)
                    if map_data[col][row] == mapTxt[0][2]:
                        map_small_bot = TutMap(self, tutMapS, col, row)
                        self.TutMap.add(map_small_bot)

        #hits -< sprite collide method 사용하여 충돌체크

    def events(self): #Event 처리에 대한
        pass

    def draw(self): #화면에 그려주는 함수
        self.TutMap.draw(self.screen)

    def show_start_screen(self): #START 화면
        self.running = True

    def show_go_screen(self): #game over, continue 화면
        pass

    def wait_for_keys(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                self.ending = True
                if event.type == pygame.QUIT:  # x를 눌렀으면
                    pygame.quit()  # terminate game
                    self.running = False
                    exit()  # exit while loop
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
                if keys[0]:
                    char_pos[1] = char_pos[1] - 20  # y값 감소 -> 위로이동
                elif keys[2]:
                    char_pos[1] = char_pos[1] + 20  # y값 증가 -> 아래로 이동
                if keys[1]:
                    char_pos[0] = char_pos[0] - 20  # x값 감소 -> 왼쪽으로 이동
                    if (char_pos[0] <= 70):
                        char_pos[0] = 70
                elif keys[3]:
                    char_pos[0] = char_pos[0] + 20  # x값 증가 -> 오른쪽으로 이동

g = Game()
while g.running:
    print("before new")
    g.new()
    print("before run")
    g.run()
pygame.quit()