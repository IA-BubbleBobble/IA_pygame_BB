import pygame
from setting import *
from sprites import *

class Game():
    def __init__(self):
        print("Game init function")
        pygame.init()
        pygame.display.init()
        pygame.mixer.init() # to use music
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # screen 크기 지정
        pygame.display.set_caption(TITLE) # 게임 창 제목표시줄에 쓰여질 문구
        self.clock = pygame.time.Clock() # 객체를 사용하여 이후 초당 프레임 설정 시 사용
        self.running = True # 게임이 끝난지 아닌지 판단 위한 변수
        self.start = True # start화면 실행, self._running -> self.start #tutorial 실행 시 false
        self.tutorial = False
        self.start_playing = True
        self.score = 0
        self.start_music = pygame.mixer.Sound("MainTheme.ogg")
        self._display_start = None
        #self.display_start = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF) #display_surf를 start로 변경

    def new(self): #game start
        print("new function")
        # sprite group
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()  # platform(tutorial map) sprite group 생성
        self.player = Player(self)  # self.character, Character 객체 생성
        self.all_sprites.add(self.player)
        # self.monsters = pygame.sprite.Group()  # monster sprite group 생성
        self.platform() # making tutorial map method
        self.run() # run game method

    def platform(self): # maker tutorial map
        for i in range(15): #  맨 윗줄
            p = Platform(tutMapStop, PLATFORM_LIST[0][0]+70*i, PLATFORM_LIST[0][1], PLATFORM_LIST[0][2], PLATFORM_LIST[0][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(8): # 왼쪽 기둥
            p = Platform(tutMapBig, PLATFORM_LIST[1][0], PLATFORM_LIST[1][1]+70*i, PLATFORM_LIST[1][2], PLATFORM_LIST[1][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(8): # 오른쪽 기둥
            p = Platform(tutMapBig, PLATFORM_LIST[2][0], PLATFORM_LIST[2][1] +70*i, PLATFORM_LIST[2][2], PLATFORM_LIST[2][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(14): # 맨 밑줄
            p = Platform(tutMapS, PLATFORM_LIST[3][0] + 70 * i, PLATFORM_LIST[3][1], PLATFORM_LIST[3][2],PLATFORM_LIST[3][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(2): # 1번째 줄(밑에서)
            p = Platform(tutMapS, PLATFORM_LIST[4][0] + 70 * i, PLATFORM_LIST[4][1], PLATFORM_LIST[4][2],PLATFORM_LIST[4][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(9): # 2번째 줄
            p = Platform(tutMapS, PLATFORM_LIST[5][0] + 70 * i, PLATFORM_LIST[5][1], PLATFORM_LIST[5][2],PLATFORM_LIST[5][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(2): # 3번째 줄
            p = Platform(tutMapS, PLATFORM_LIST[6][0] + 70 * i, PLATFORM_LIST[6][1], PLATFORM_LIST[6][2],PLATFORM_LIST[6][3])
            self.all_sprites.add(p)
            self.platforms.add(p)

    def run(self): #게임 갱신
        print("run function")
        # game loop
        # back ground music 설정도 여기서
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        print("update function")
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                print("hits!============================")
                self.player.pos.y = hits[0].rect.top + 0.1
                self.player.vel.y = 0

    def events(self): #Event 처리에 대한
        print("event function")
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    pygame.quit()
                    self.playing = False
                    exit()  # exit while loop
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.jump()

    def draw(self): #화면에 그려주는 함수
        print('draw function')
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        #self.screen.blit(self.player.image, player_pos)
        pygame.display.flip()  # 화면 초기화

# ============================START=============================
    def printword_white(self,size, word,location): # making letter white function
        font = pygame.font.Font(BUBBLE_FONT,size)
        text = font.render(word,True,WHITE)
        self.screen.blit(text, location)

    def on_cleanup(self):
        self.running = False
        pygame.quit()
        exit() # pygame.quit() 후에 꼭 exit()해야한다 -> surface exit error

    def show_start_screen(self):
        print('show_start_screen function')
        self.running = True
        self.start_music.play()
        self.start_run()

    def start_run(self):
        print("start_run function")
        while self.start_playing:
            self.clock.tick(FPS)
            self.start_draw()

    def start_draw(self): #START 화면
        print("start_draw function")
        color = 1
        progress_sec = 0
        while (True):
            progress_sec += 1
            self.screen.fill(WHITE)
            self.loadimage(START_SCREEND, (0, 0))
            string_score = "00"
            if (self.score != 0):
                string_score = str(self.score)
            self.printword_white(18, string_score, (175, 56))
            self.printword_white(18, "A.START            B.TUTORIAL", (273, 600))
            # self.printword_white(18,string_score,(490,56))
            if (progress_sec > 60):
                if (color == 1):
                    self.loadimage(PINK_SUPERBUBBLE, (260, 70))
                    color = 0
                else:
                    self.loadimage(YELLOW_SUPERBUBBLE, (260, 70))
                    color = 1
            else:
                if (color == 1):
                    self.loadimage(PINK_BUBBLE, (260, 70))
                    color = 0
                else:
                    self.loadimage(YELLOW_BUBBLE, (260, 70))
                    color = 1
            pygame.display.flip()
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.on_cleanup()
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_a):
                        print("a")
                        break
                    elif (event.key == pygame.K_b):
                        print('b')
                        self.tutorial = True # tutorial 실행
                        break

            if (self.tutorial):
                self.start_music.stop()
                self.start_playing = False
                break

    def loadimage(self,image,location): # image load function
        load_image = pygame.image.load(image).convert()
        self.screen.blit(load_image,location)

    def show_go_screen(self): #game over, continue 화면
        print('show_go_screen fuction')

    def wait_for_keys(self):
        print('wait_for_keys function')
        waiting = True
        # while waiting:
        #     self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # x를 눌렀으면
                pygame.quit()  # terminate game
                waiting = False
                #self.running = False
                exit()  # exit while loop
            if event.type == pygame.KEYDOWN:  # key가 눌려지는 type의 event이면
                if event.key == pygame.K_UP:  # 위쪽 방향키가 눌려지면
                    keys[0] = True
                elif event.key == pygame.K_LEFT:  # 왼쪽 방향키가 눌려지면
                    keys[1] = True
                if event.key == pygame.K_SPACE:  # 스페이스키가 눌려지면
                    keys[2] = True
                if event.key == pygame.K_RIGHT:  # 오른쪽 방향키가 눌려지면
                    keys[3] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:  # 위쪽 방향키를 떼면
                    keys[0] = False
                elif event.key == pygame.K_LEFT:  # 왼쪽 방향키를 떼면
                    keys[1] = False
                if event.key == pygame.K_SPACE:  # 스페이스키를 떼면
                    keys[2] = False
                if event.key == pygame.K_RIGHT:  # 오른쪽 방향키를 떼면
                    keys[3] = False
        if keys[0]:
            #char_jump() # 캐릭터 점프
            player_pos[1] = player_pos[1] // 2
        # elif keys[2]:
        #     shoot_bubble()
        if keys[1]:
            player_pos[0] = player_pos[0] - 20  # x값 감소 -> 왼쪽으로 이동
            if (player_pos[0] <= 70):
                player_pos[0] = 70
        elif keys[3]:
            player_pos[0] = player_pos[0] + 20  # x값 증가 -> 오른쪽으로 이동

g = Game()
while g.start:
    g.show_start_screen()
    while g.running:
        g.new()
pygame.quit()