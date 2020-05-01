import pygame
from pygame.locals import *
import time
import keyboard
import sys

class Bubble:
    def __init__(self):
        WHITE = {255, 255,255}
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1050, 700
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
    
    def loadimage(self,image,location):
        load_image = pygame.image.load(image).convert()
        self._display_surf.blit(load_image,location)   

    def start(self):
        start_background = pygame.mixer.Sound("MainTheme.ogg")
        start_background.play()
        

        self.loadimage("./image/start.png",(0,0))
        pygame.display.flip()

        press = True
        color = 1
        progress_sec=0
        while press:
            progress_sec +=1

            if(color == 1):
                self.loadimage('image/pink_bubble.png',(0,0))
                color = 0
            else:
                self.loadimage('image/yellow_bubble.png',(0,0))
                color = 1
            pygame.display.flip()
            self.clock.tick(120)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_1] :
                print('1')
                press = False
            elif keys[pygame.K_2] :
                print('2')
                press = False
            
            if(progress_sec > 100):
                press = False
        start_background.stop()

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

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.start()
            self.on_loop()
            self.on_render()
            
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = Bubble()
    theApp.on_execute()