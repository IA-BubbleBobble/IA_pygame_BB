import pygame

#base properties
TITLE = "Bubble Bobble"
WIDTH = 1050
HEIGHT = 700
FPS = 60

TILESIZE = 70
CHARSIZE = 45

#Font
BUBBLE_FONT = "PressStart2P.ttf"

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)
BROWN = (111, 109, 81)

# key (pushed or not)
keys = [False, False, False, False, False] # [K_UP(jump), K_LEFT(move left), K_SPACE(shoot bubble), K_RIGHT(move right)]

#Player properties
player_pos = [70, 620]
bubble_pos = [80, 630]
PLAYER_ACC = 1.5
PLAYER_FRICTION = -0.2
PLAYER_GRAVITY = 0.8
PLAYER_JUMP = 15.5

#Monstar properties
MONSTAR_ACC = 0.5
MONSTAR_FRICTION = -0.2

# Image
charL1 = "image/charL1.png" # character 왼쪽 이동시 움직임1
charL2 = "image/charL2.png" # character 왼쪽 이동시 움직임2
charL3 = "image/charL3.png" # character 왼쪽 이동시 움직임3
charL4 = "image/charL4.png" # character 왼쪽 이동시 움직임4
charR1 = "image/charR1.png" # character 왼쪽 이동시 움직임1
charR2 = "image/charR2.png" # character 왼쪽 이동시 움직임2
charR3 = "image/charR3.png" # character 왼쪽 이동시 움직임3
charR4 = "image/charR4.png" # character 왼쪽 이동시 움직임4
tutMapBig = "image/tutMapBig.PNG" # tutorial map big block
tutMapStop = "image/tutMapStop.PNG" # tutorial map small block(위쪽이 검은색)
tutMapS = "image/tutMapS.PNG" # only small red block
s1MapBig = "image/s1MapBig.PNG"
s1MapStop = "image/s1MapStop.PNG"
s1MapS = "image/s1MapS.PNG"
s2MapBig = "image/s2MapBig.PNG"
s2MapStop = "image/s2MapStop.PNG"
s2MapS = "image/s2MapS.PNG"
s3MapBig = "image/s3MapBig.png"
s3MapStop = "image/s3MapStop.PNG"
s3MapS = "image/s3MapS.PNG"
charL = [charL1, charL2, charL3, charL3]
charR = [charR1, charR2, charR3, charR3]
bubble1 = "image/bubble1.png"
bubble2 = "image/bubble2.png"
bubble3 = "image/bubble3.png"
bubble4 = "image/bubble4.png"
plymonL = "image/plymonL.png"
plymonR = "image/plymonR.png"

YELLOW_BUBBLE = "./image/yellow_bubble.png"
PINK_BUBBLE = "./image/pink_bubble.png"
YELLOW_SUPERBUBBLE = "./image/yellow_superbubble.png"
PINK_SUPERBUBBLE = "./image/pink_superbubble.png"
START_SCREEND = "./image/start.png"
ENDING_IMAGE = "./image/end.png"
YELLOW_HEART = "./image/yellow_last.png"
ORANGE_HEART = "./image/orange_last.png"
RED_HEART = "./image/red_last.png"
PINK_HEART = "./image/pink_last.png"
S_YELLOW_HEART = "./image/s_yellow_last.png"
S_ORANGE_HEART = "./image/s_orange_last.png"
S_RED_HEART = "./image/s_red_last.png"
S_PINK_HEART = "./image/s_pink_last.png"
monstarLD = './image/monstarLD.png' # 몬스터가 왼쪽으로 움직일 때 움직임 1
monstarLU = './image/monstarLU.png' # 몬스터가 왼쪽으로 움직일 때 움직임 2
monstarRD = "./image/monstarRD.png" # 몬스터가 오른쪽으로 움직일 때 움직임 1
monstarRU = "./image/monstarRU.png" # 몬스터가 오른쪽으로 움직일 때 움직임 2
monstarDL1 = "./image/monstarDL1.png" # 몬스터가 죽었을때 왼쪽을 움직일 때 움직임 1"
monstarDL2 = "./image/monstarDL2.png" # 몬스터가 죽었을때 왼쪽을 움직일 때 움직임 2"
monstarDL3 = "./image/monstarDL3.png" # 몬스터가 죽었을때 왼쪽을 움직일 때 움직임 3"
monstarDL4 = "./image/monstarDL4.png" # 몬스터가 죽었을때 왼쪽을 움직일 때 움직임 4"
monstarDR1 = "./image/monstarDR1.png" # 몬스터가 죽었을때 오른쪽을 움직일 때 움직임 1"
monstarDR2 = "./image/monstarDR2.png" # 몬스터가 죽었을때 오른쪽을 움직일 때 움직임 2"
monstarDR3 = "./image/monstarDR3.png" # 몬스터가 죽었을때 오른쪽을 움직일 때 움직임 3"
monstarDR4 = "./image/monstarDR4.png" # 몬스터가 죽었을때 오른쪽을 움직일 때 움직임 4"
item_dic = {'banana':'./image/item_icon/banana.png', 'orange':'./image/item_icon/orange.png', 'strawberry':'./image/item_icon/strawberry.png',
'watermelon':'./image/item_icon/watermelon.png', 'shell':'./image/item_icon/shell.png', 'pudding':'./image/item_icon/pudding.png'}
EMPTY = "image/empty.png" # item이 몬스터가 죽어서 날라가서 사라진후 나오기 위해 empty에서 item으로 바뀔 때 사용
LIFE1 = 'image/life1.png'
LIFE2 = 'image/life2.png'
LIFE3 = 'image/life3.png'
LIFE0 = 'image/empty_heart.png'
monstarBb = "image/green_monstar_bubble2.png" # 몬스터가 버블에 갇혔을 때
pon = 'image/pon.png'

#sound
pygame.mixer.init() # to use music
mainTheme = pygame.mixer.Sound("sound/MainTheme.ogg")
playerJump = pygame.mixer.Sound("sound/playerJump.wav")
gameStart = pygame.mixer.Sound("sound/GameStart.ogg")
shootBubble = pygame.mixer.Sound("sound/shootBubble.wav")
gameOver = pygame.mixer.Sound("sound/GameOver.ogg")
gameComplete = pygame.mixer.Sound("sound/GameTurnedOn.ogg")



# about map
mapFile = ["map/tut_map.txt", "map/stage1_map.txt"]
mapTxt = [("q", "a", "z"), ("q", "a", "z")] # (big, small_top, small_bottom, shadow)
mapImage = [(tutMapBig, tutMapStop, tutMapS), (s1MapBig, s1MapStop, s1MapS), (s2MapBig, s2MapStop, s2MapS), (s3MapBig, s3MapStop, s3MapS)] # (big, small_top, small_bottom)
PLATFORM_LIST = [(0,70,TILESIZE, TILESIZE), (0,140, TILESIZE, TILESIZE), (70*14,140, TILESIZE, TILESIZE), (70, 675, 70, 25),
                 (70*3, 70*8, 70, 25), (70*3, 70*6+25, 70, 25), (70*10, 70*4+35, 70, 25)] # tutorial map
PLATFORM1_LIST = [(0,70,TILESIZE, TILESIZE), (0,140, TILESIZE, TILESIZE), (70*14,140, TILESIZE, TILESIZE), (70, 675, 70, 25),
                 (70, 70*8, 70, 25), (70, 70*6+25, 70, 25), (70, 70*4+35, 70, 25)] # stage1 map
PLATFORM2_LIST = [(0,70,TILESIZE, TILESIZE), (0,140, TILESIZE, TILESIZE), (70*14,140, TILESIZE, TILESIZE), (70, 675, 70, 25),
                 (70, 70*9-45, 70, 25), (70, 70*7-35, 70, 25), (70, 70*5, 70, 25), (70, 70*4-35, 70, 25)] # stage2 map
PLATFORM3_LIST = [(0,70,TILESIZE, TILESIZE), (0,140, TILESIZE, TILESIZE), (70*14,140, TILESIZE, TILESIZE), (70, 675, 70, 25),
                  (70, 70 * 8, 70, 25), (70, 70 * 6 + 35, 70, 25), (70, 70 * 5, 70, 25), (70, 70 * 3, 70, 25)] # stage3 map
