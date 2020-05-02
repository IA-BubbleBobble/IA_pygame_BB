import pygame
from setting import *
from sprites import *
import time

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
        self.high_score = 0
        self.start_music = pygame.mixer.Sound("MainTheme.ogg")
        self._display_start = None
        self.end_music = pygame.mixer.Sound("./music/GameEnding.ogg")
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
        pass

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
        # 재시작하였을 때 다시 시작하기 전 점수를 high_score에 넣어준다.
        if(self.score> self.high_score):
            self.high_score = self.score
        #재시작하는 경우를 생각해서 score를 초기화 시켜준다.
        self.score = 0
        color = 1
        progress_sec = 0
        while (True):
            progress_sec += 1
            self.screen.fill(WHITE)
            self.loadimage(START_SCREEND, (0, 0))
            string_score = "00"
            string_high_score = "00"
            # 만약에 self.score가 0이면 00을 print 해주기 위해서 비교
            if(self.score !=0):
                string_score = str(self.score)
            if(self.high_score !=0):
                string_high_score = str(self.high_score)
            self.printword_white(18,string_score,(175,56))
            self.printword_white(18,"A.START            B.TUTORIAL",(273,600))
            self.printword_white(18,str(string_high_score),(490,56))
            #color 변수를 사용하여 두개의 이미지를 번갈아가면 수행시켜 준다
            if(progress_sec>60):
                if(color == 1):
                    self.loadimage(PINK_SUPERBUBBLE,(260,70))
                    color = 0
                else:
                    self.loadimage(YELLOW_SUPERBUBBLE,(260,70))
                    color = 1
            else:
                if(color == 1):
                    self.loadimage(PINK_BUBBLE,(260,70))
                    color = 0
                else:
                    self.loadimage(YELLOW_BUBBLE,(260,70))
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
        # 시작 7초후에 continue화면을 띄워주기 위해 시작할 때 현재 시간 저장
        self.start_playing = False #재시작 할 때 True로 바꾸기 위해
        start_time = time.time()
        self.end_music.play() 

        color = 1
        while(True):
            now_time = time.time()
            progress_sec = now_time - start_time
            self.screen.fill(WHITE)
            self.loadimage(ENDING_IMAGE,(0,0))
            # 4개의 이미지를 반복적으로 수행
            if(color % 4 == 1) :
                self.loadimage(YELLOW_HEART,(360,155))
                self.loadimage(S_YELLOW_HEART,(0,580))
            elif(color % 4 ==2):
                self.loadimage(ORANGE_HEART,(360,155))
                self.loadimage(S_ORANGE_HEART,(0,580))
            elif(color % 4 ==3):
                self.loadimage(RED_HEART,(360,155))
                self.loadimage(S_RED_HEART,(0,580))
            else:
                self.loadimage(PINK_HEART,(360,155))
                self.loadimage(S_PINK_HEART,(0,580))
            color += 1
            string_score = "00"
            # 만약에 self.score가 0이면 00을 print 해주기 위해서 비교
            if(self.score !=0):
                string_score = str(self.score)
            # 현재 플레이어의 점수 화면에 출력
            self.printword_white(18,string_score,(175,56))
            # 현재 플레이어의 최고 점수를 화면에 출력
            self.printword_white(18,str(self.high_score),(490,56))
            # 화면에 메인으로 보여질 점수를 가운데에 출력하기 위해 구하는 변수
            word_location = 1050/2 - (len(string_score)/2)*70 +13
            self.printword_white(36,string_score,(word_location,140))
            #7초후부터 continue 화면 출력
            if(progress_sec >= 7):
                self.printword_white(22,"A.RESTART           B.EXIT",(249,640))
            pygame.display.flip()
            # 7초후부터 continue 화면에 대해서 a키를 누르면 시작화면으로, b키를 누르면 게임을 종료하게 된다.
            if(progress_sec >= 7):
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if(event.key ==pygame.K_a):
                            self.start_playing = True # 재시작을 한다.
                            print('a')
                            break
                        elif(event.key == pygame.K_b):
                            print('b')
                            self.end_music.stop()
                            self.on_cleanup()
                            break
            
            if(self.start_playing):
                self.end_music.stop()
                self.show_start_screen()
                break

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
    #g.show_start_screen()
    g.show_go_screen()
    while g.running:
        g.new()
pygame.quit()