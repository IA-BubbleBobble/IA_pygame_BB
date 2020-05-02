import pygame
from setting import *
from sprites import *

class Game():
    def __init__(self):
        print("Game init function")
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # screen 크기 지정
        pygame.display.set_caption(TITLE) # 게임 창 제목표시줄에 쓰여질 문구
        self.clock = pygame.time.Clock() # 객체를 사용하여 이후 초당 프레임 설정 시 사용
        self.running = True # 게임이 끝난지 아닌지 판단 위한 변수
        self.start = True # start화면 실행, self._running -> self.start #tutorial 실행 시 false
        self.tutorial = False # tutorial 실행 여부
        self.stage1 = False # stage1 실행 여부
        self.stage2 = False # stage2 실행 여부
        self.start_playing = True
        self.score = 0
        self._display_start = None

    def new(self): #game start
        print("new function")
        # sprite group
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()  # platform(tutorial map) sprite group 생성
        if(self.tutorial == True): # 현재 tutorial 을 실행 할 차례면 tutorial map을 만든다
            self.platform() # making tutorial map method
        elif(self.stage1 == True): # stage1을 실행 할 차례면 stage1 map을 만든다
            self.platform1()  # making stage1 map method
        elif(self.stage2 == True): # stage2 를 실행 할 차례면 stage2 map을 만든다
            self.platform2()  # making stage1 map method
        self.player = Player(self)  # self.character, Character 객체 생성
        self.all_sprites.add(self.player)
        # self.monsters = pygame.sprite.Group()  # monster sprite group 생성
        gameStart.play(-1)
        self.run() # run game method

    def platform(self): # make tutorial map
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

    def platform1(self): # make stage1 map
        for i in range(15): #  맨 윗줄
            p = Platform(s1MapStop, PLATFORM1_LIST[0][0]+70*i, PLATFORM1_LIST[0][1], PLATFORM1_LIST[0][2], PLATFORM1_LIST[0][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(8): # 왼쪽 기둥
            p = Platform(s1MapBig, PLATFORM1_LIST[1][0], PLATFORM1_LIST[1][1]+70*i, PLATFORM1_LIST[1][2], PLATFORM1_LIST[1][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(8): # 오른쪽 기둥
            p = Platform(s1MapBig, PLATFORM1_LIST[2][0], PLATFORM1_LIST[2][1] +70*i, PLATFORM1_LIST[2][2], PLATFORM1_LIST[2][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(13): # 맨 밑줄
            p = Platform(s1MapS, PLATFORM1_LIST[3][0] + 70 * i, PLATFORM1_LIST[3][1], PLATFORM1_LIST[3][2],PLATFORM1_LIST[3][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(13): # 1번째 줄(밑에서)
            if(i != 1 and i != 2 and i !=10 and i != 11):
                p = Platform(s1MapS, PLATFORM1_LIST[4][0] + 70 * i, PLATFORM1_LIST[4][1], PLATFORM1_LIST[4][2],PLATFORM1_LIST[4][3])
                self.all_sprites.add(p)
                self.platforms.add(p)
                p = Platform(s1MapS, PLATFORM1_LIST[5][0] + 70 * i, PLATFORM1_LIST[5][1], PLATFORM1_LIST[5][2],PLATFORM1_LIST[5][3])
                self.all_sprites.add(p)
                self.platforms.add(p)
                p = Platform(s1MapS, PLATFORM1_LIST[6][0] + 70 * i, PLATFORM1_LIST[6][1], PLATFORM1_LIST[6][2],PLATFORM1_LIST[6][3])
                self.all_sprites.add(p)
                self.platforms.add(p)

    def platform2(self): # make stage2 map
        for i in range(15):  # 맨 윗줄
            p = Platform(s2MapStop, PLATFORM2_LIST[0][0]+70*i, PLATFORM1_LIST[0][1], PLATFORM1_LIST[0][2], PLATFORM1_LIST[0][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(8): # 왼쪽 기둥
            p = Platform(s2MapBig, PLATFORM2_LIST[1][0], PLATFORM1_LIST[1][1]+70*i, PLATFORM1_LIST[1][2], PLATFORM1_LIST[1][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(8): # 오른쪽 기둥
            p = Platform(s2MapBig, PLATFORM2_LIST[2][0], PLATFORM1_LIST[2][1] +70*i, PLATFORM1_LIST[2][2], PLATFORM1_LIST[2][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(13): # 맨 밑줄
            p = Platform(s2MapS, PLATFORM2_LIST[3][0] + 70 * i, PLATFORM1_LIST[3][1], PLATFORM1_LIST[3][2],PLATFORM1_LIST[3][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(13):
            if (i != 0 and i != 4 and i != 8 and i != 12):
                p = Platform(s2MapS, PLATFORM2_LIST[4][0] + 70 * i, PLATFORM2_LIST[4][1], PLATFORM2_LIST[4][2],PLATFORM2_LIST[4][3])
                self.all_sprites.add(p)
                self.platforms.add(p)
            if (i != 0 and i != 1 and i != 11 and i != 12):
                p = Platform(s2MapS, PLATFORM2_LIST[5][0] + 70 * i, PLATFORM2_LIST[5][1], PLATFORM2_LIST[5][2],PLATFORM2_LIST[5][3])
                self.all_sprites.add(p)
                self.platforms.add(p)
            if (i != 0 and i != 1 and i != 2 and i != 6 and i != 10 and i != 11 and i != 12):
                p = Platform(s2MapS, PLATFORM2_LIST[6][0] + 70 * i, PLATFORM2_LIST[6][1], PLATFORM2_LIST[6][2],PLATFORM2_LIST[6][3])
                self.all_sprites.add(p)
                self.platforms.add(p)
            if (i != 0 and i != 1 and i != 2 and i != 3 and i != 9 and i != 10 and i != 11 and i != 12):
                p = Platform(s2MapS, PLATFORM2_LIST[7][0] + 70 * i, PLATFORM2_LIST[7][1], PLATFORM2_LIST[7][2],PLATFORM2_LIST[7][3])
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
                self.player.pos.y = hits[0].rect.y-45 + 0.1 # 벽돌위로
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
                    playerJump.play()
                    self.player.jump()


    def draw(self): #화면에 그려주는 함수
        print('draw function')
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
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

    def show_start_screen(self): # music play and call start_run function
        print('show_start_screen function')
        #self.running = True
        mainTheme.play()
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
                    if (event.key == pygame.K_a): # a를 누르면 stage1 실행
                        print("a")
                        self.stage1 = True
                        break
                    elif (event.key == pygame.K_b):
                        print('b')
                        self.tutorial = True # b를 누르면 tutorial 실행
                        break

            if (self.tutorial): # tutorial을 실행 할 차례면
                mainTheme.stop() # start 음악을 멈추고
                self.start_playing = False # start screen을 띄우는 while loop를 벗어난다
                break

            elif (self.stage1):
                mainTheme.stop()  # start 음악을 멈추고
                self.start_playing = False  # start screen을 띄우는 while loop를 벗어난다
                break

    def loadimage(self,image,location): # image load function
        load_image = pygame.image.load(image).convert()
        self.screen.blit(load_image,location)

    def show_go_screen(self): #game over, continue 화면
        print('show_go_screen fuction')

g = Game()
while g.start:
    g.show_start_screen()
    while g.running:
        g.new()
pygame.quit()