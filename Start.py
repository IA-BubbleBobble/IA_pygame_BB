import pygame
from setting import *
from sprites import *
import time
import time

class Game():
    def __init__(self):
        print("Game init function")
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # screen 크기 지정
        pygame.display.set_caption(TITLE) # 게임 창 제목표시줄에 쓰여질 문구
        self.clock = pygame.time.Clock() # 객체를 사용하여 이후 초당 프레임 설정 시 사용
        self.running = True # 게임이 끝난지 아닌지 판단 위한 변수
        self.start = True # start 화면 실행, self._running -> self.start #tutorial 실행 시 false
        self.tutorial = False # tutorial 실행 여부
        self.stage1 = False # stage1 실행 여부
        self.stage2 = False # stage2 실행 여부
        self.stage3 = False # stage3 실행 여부
        self.ending = False # ending 화면 실행
        self.start_playing = True # run함수 돌리는거. False되면 new로 돌아가 새로운 platform 그림
        self.playerHealth = 3 # player목숨 3개
        self.score = 0
        self.high_score = 0
        self._display_start = None
        self.playerCollide = False
        self.lr = 1 # 0이면 player가 왼쪽보는거, 1이면 player가 오른쪽 보는거

    def new(self): #game start
        print("new function")
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()  # platform(tutorial map) sprite group 생성
        self.bubble = pygame.sprite.Group()  # platform(tutorial map) sprite group 생성
        self.player = Player(self)  # self.character, Character 객체 생성
        self.monster = pygame.sprite.Group()
        if(self.tutorial == True): # 현재 tutorial 을 실행 할 차례면 tutorial map을 만든다
            self.platform() # making tutorial map method
            monster_x = 700
            for i in range(3): # tutorial에서는 monster 3마리만
                m = Monster(self, (monster_x, 200), 'left', 'live')  # (game, location, direction, state)
                monster_x -= 50
                self.monster.add(m)
                self.all_sprites.add(m)
            self.tutorial, self.stage1 = False, True
        elif(self.stage1 == True): # stage1을 실행 할 차례면 stage1 map을 만든다
            self.platform1()  # making stage1 map method
        elif(self.stage2 == True): # stage2 를 실행 할 차례면 stage2 map을 만든다
            self.platform2()  # making stage1 map method
        elif(self.stage3 == True):
            self.platform3() # making stage3 map method
        elif(self.ending == True):
            self.show_go_screen() # ending page
        self.player = Player(self)  # self.character, Character 객체 생성
        self.all_sprites.add(self.player)
        if(self.ending == False):
            gameStart.play(-1) #음악 계속 실행
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

    # ------------ stage3 map 조금 수정 필요! (맨밑 for문 수정, jump할 때 걸리지 않는 높이로 조정부탁)
    def platform3(self):  # make stage3 map
        for i in range(15):  # 맨 윗줄
            p = Platform(s3MapStop, PLATFORM3_LIST[0][0] + 70 * i, PLATFORM1_LIST[0][1], PLATFORM1_LIST[0][2],
                         PLATFORM1_LIST[0][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(8):  # 왼쪽 기둥
            p = Platform(s3MapBig, PLATFORM3_LIST[1][0], PLATFORM1_LIST[1][1] + 70 * i, PLATFORM1_LIST[1][2],
                         PLATFORM1_LIST[1][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(8):  # 오른쪽 기둥
            p = Platform(s3MapBig, PLATFORM3_LIST[2][0], PLATFORM1_LIST[2][1] + 70 * i, PLATFORM1_LIST[2][2],
                         PLATFORM1_LIST[2][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(13):  # 맨 밑줄
            p = Platform(s3MapS, PLATFORM3_LIST[3][0] + 70 * i, PLATFORM1_LIST[3][1], PLATFORM1_LIST[3][2],
                         PLATFORM1_LIST[3][3])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(13):
            if (i != 6 and i != 7):  # 밑에서 첫번째
                p = Platform(s3MapS, PLATFORM3_LIST[4][0] + 70 * i, PLATFORM3_LIST[4][1], PLATFORM3_LIST[4][2],
                             PLATFORM3_LIST[4][3])
                self.all_sprites.add(p)
                self.platforms.add(p)
            if (i != 0 and i != 1 and i != 2 and i != 3 and i != 9 and i != 10 and i != 11 and i != 12):  # 밑에서 두번째
                p = Platform(s3MapS, PLATFORM3_LIST[5][0] + 70 * i, PLATFORM3_LIST[5][1], PLATFORM3_LIST[5][2],
                             PLATFORM3_LIST[5][3])
                self.all_sprites.add(p)
                self.platforms.add(p)
            if (i != 5 and i != 6 and i != 3 and i != 12):
                p = Platform(s3MapS, PLATFORM3_LIST[6][0] + 70 * i, PLATFORM3_LIST[6][1], PLATFORM3_LIST[6][2],
                             PLATFORM3_LIST[6][3])
                self.all_sprites.add(p)
                self.platforms.add(p)
            if (i != 1 and i != 2 and i != 3 and i != 4 and i != 8 and i !=9 and i != 10 and i != 11):
                p = Platform(s3MapS, PLATFORM3_LIST[7][0] + 70 * i, PLATFORM3_LIST[7][1], PLATFORM3_LIST[7][2],
                             PLATFORM3_LIST[7][3])
                self.all_sprites.add(p)
                self.platforms.add(p)
            if (i != 5 and i != 6 and i != 7):
                p = Platform(s3MapS, PLATFORM3_LIST[7][0] + 70 * i, PLATFORM3_LIST[7][1], PLATFORM3_LIST[7][2],
                             PLATFORM3_LIST[7][3])
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
            self.update() #lr, bubmon
            self.draw()

    def update(self):
        print("update function")
        self.all_sprites.update()
        print('finish player in update')
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                print("hits!============================")
                self.player.pos.y = hits[0].rect.y-45 + 0.1 # 벽돌위로
                self.player.vel.y = 0

        # 버블 객체를 bubble이라고 가정했을 때 , 충돌 하는거!!!!!!!!!!!!충돌되었는지 아닌지 인식못함...ㅜㅜ
        bubmon_hits = pygame.sprite.groupcollide(self.bubble, self.monster, False, True, pygame.sprite.collide_mask)
        if bubmon_hits:
            for hit in bubmon_hits:
                print(("------------------bubble and monster hit!------------------------------"))
                m = Monster(self, (hit.rect.x, hit.rect.y), 'left', 'dead')
                #expl = Explosion(self, hit.rect.center)
                self.score += 1  # 점수를 1점 증가시킴
                if (self.score == 3):
                    self.tutorial = False
                    self.stage1 = True
                    self.playing = False # map 변경할 때 필요

        # monster가 player와 부딪혔을 때
        plymon = pygame.sprite.spritecollide(self.player, self.monster, False, pygame.sprite.collide_mask) # True 하면 닿이면 사라짐
        if (plymon):
            print("player and monster collide!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
            self.playerCollide = True
            self.playerHealth -= 1
            if(self.playerHealth == 0):
                self.tutorial = self.stage1 = self.stage2 = self.playing = False # 모든걸 중지
                self.ending = True # ending 화면으로


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
                if event.key == pygame.K_SPACE:
                    shootBubble.play()
                    bb = Bubble(self, self.lr, self.player.rect.x, self.player.rect.y) # 마지막 bubble
                    self.all_sprites.add(self.bubble)
                    self.bubble.add(bb)


    def draw(self): #화면에 그려주는 함수
        print('draw function')
        self.screen.fill(BLACK)
        self.monster.draw(self.screen)
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
        # 재시작하였을 때 다시 시작하기 전 점수를 high_score에 넣어준다.
        if (self.score > self.high_score):
            self.high_score = self.score
        # 재시작하는 경우를 생각해서 score를 초기화 시켜준다.
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
            if (self.score != 0):
                string_score = str(self.score)
            if (self.high_score != 0):
                string_high_score = str(self.high_score)
            self.printword_white(18, string_score, (175, 56))
            self.printword_white(18, "A.START            B.TUTORIAL", (273, 600))
            self.printword_white(18, str(string_high_score), (490, 56))
            # color 변수를 사용하여 두개의 이미지를 번갈아가면 수행시켜 준다
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

    # -------------마지막 화면 하트이미지 하나 수정, stage도중에 끝났을 때 ending page 만들어주세용
    def show_go_screen(self): #game over, continue 화면 # -------------마지막 화면 하트이미지 하나 수정, stage도중에 끝났을 때 ending page 만들어주세용
        print('show_go_screen fuction')
        # 시작 7초후에 continue화면을 띄워주기 위해 시작할 때 현재 시간 저장
        self.start_playing = False  # 재시작 할 때 True로 바꾸기 위해
        start_time = time.time()
        gameOver.play()

        color = 1
        while (True):
            now_time = time.time()
            progress_sec = now_time - start_time
            self.screen.fill(WHITE)
            self.loadimage(ENDING_IMAGE, (0, 0))
            # 4개의 이미지를 반복적으로 수행
            if (color % 4 == 1):
                self.loadimage(YELLOW_HEART, (360, 155))
                self.loadimage(S_YELLOW_HEART, (0, 580))
            elif (color % 4 == 2):
                self.loadimage(ORANGE_HEART, (360, 155))
                self.loadimage(S_ORANGE_HEART, (0, 580))
            elif (color % 4 == 3):
                self.loadimage(RED_HEART, (360, 155))
                self.loadimage(S_RED_HEART, (0, 580))
            else:
                self.loadimage(PINK_HEART, (360, 155))
                self.loadimage(S_PINK_HEART, (0, 580))
            color += 1
            string_score = "00"
            # 만약에 self.score가 0이면 00을 print 해주기 위해서 비교
            if (self.score != 0):
                string_score = str(self.score)
            # 현재 플레이어의 점수 화면에 출력
            self.printword_white(18, string_score, (175, 56))
            # 현재 플레이어의 최고 점수를 화면에 출력
            self.printword_white(18, str(self.high_score), (490, 56))
            # 화면에 메인으로 보여질 점수를 가운데에 출력하기 위해 구하는 변수
            word_location = 1050 / 2 - (len(string_score) / 2) * 70 + 13
            self.printword_white(36, string_score, (word_location, 140))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # 7초후부터 continue 화면 출력
            if (progress_sec >= 7):
                self.printword_white(22, "A.RESTART           B.EXIT", (249, 640))
            pygame.display.flip()
            # 7초후부터 continue 화면에 대해서 a키를 누르면 시작화면으로, b키를 누르면 게임을 종료하게 된다.
            if (progress_sec >= 7):
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_a):
                            self.start_playing = True  # 재시작을 한다.
                            print('a')
                            break
                        elif (event.key == pygame.K_b):
                            print('b')
                            gameOver.stop()
                            self.on_cleanup()
                            break

            if (self.start_playing):
                gameOver.stop()
                self.show_start_screen()
                break
g = Game()
while g.start:
    g.show_start_screen()
    while g.running:
        g.new()
pygame.quit()