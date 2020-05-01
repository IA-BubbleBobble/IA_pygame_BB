import pygame
from pygame.locals import *
import time
from settings import *
from sprites import *

class Bubble:
    def __init__(self):
        WHITE = {255, 255,255}
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = WIDTH, HEIGHT
        self.clock = pygame.time.Clock()
        self.score = 0
        self.high_score = 0

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
    
    def loadimage(self,image,location):
        load_image = pygame.image.load(image).convert()
        self._display_surf.blit(load_image,location)

    def printword_white(self,size, word,location):
        font = pygame.font.Font(BUBBLE_FONT,size)
        text = font.render(word,True,WHITE)
        self._display_surf.blit(text,location)   

    def show_start_screen(self):
        # 재시작하였을 때 다시 시작하기 전 점수를 high_score에 넣어준다.
        if(self.score> self.high_score):
            self.high_score = self.score
        #재시작하는 경우를 생각해서 score를 초기화 시켜준다.
        self.score = 0
        start_music = pygame.mixer.Sound("MainTheme.ogg")
        start_music.play()

        color = 1
        progress_sec=0
        while(True):
            progress_sec +=1
            self._display_surf.fill(WHITE)
            self.loadimage(START_SCREEND,(0,0))
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

            if(progress_sec >= 7):
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if(event.key ==pygame.K_a):
                            start_music.stop()
                            print('a')
                            break
                        elif(event.key == pygame.K_b):
                            start_music.stop()
                            print('b')
                            break
            
            if(progress_sec > 200):
                start_music.stop()
                break

    def show_end_screen(self):
        # 시작 7초후에 continue화면을 띄워주기 위해 시작할 때 현재 시간 저장
        start_time = time.time()

        end_music = pygame.mixer.Sound("./music/GameEnding.ogg") 
        end_music.play() 

        color = 1
        while(True):
            now_time = time.time()
            progress_sec = now_time - start_time
            print(progress_sec)
            self._display_surf.fill(WHITE)
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
            #self.clock.tick(FPS)

            # 7초후부터 continue 화면에 대해서 a키를 누르면 시작화면으로, b키를 누르면 게임을 종료하게 된다.
            if(progress_sec >= 7):
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if(event.key ==pygame.K_a):
                            end_music.stop()
                            self.show_start_screen()
                            break
                        elif(event.key == pygame.K_b):
                            end_music.stop()
                            self.on_cleanup()
                            break

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()

        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        self.show_end_screen()            
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = Bubble()
    theApp.on_execute()