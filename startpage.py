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
        start_music = pygame.mixer.Sound("MainTheme.ogg")
        start_music.play()

        color = 1
        progress_sec=0
        while(True):
            progress_sec +=1
            self._display_surf.fill(WHITE)
            self.loadimage(START_SCREEND,(0,0))
            string_score = "00"
            if(self.score !=0):
                string_score = str(self.score)
            self.printword_white(18,string_score,(175,56))
            self.printword_white(18,"A.START            B.TUTORIAL",(273,600))
            #self.printword_white(18,string_score,(490,56))
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
                if(event.type ==pygame.K_a):
                    print("a")
                    break
                elif(event.type == pygame.K_b):
                    print('b')
                    break
            
            if(progress_sec > 200):
                break
        start_music.stop()

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
        self.show_start_screen()            
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = Bubble()
    theApp.on_execute()