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
PLAYER_ACC = 1.5
PLAYER_FRICTION = -0.2
PLAYER_GRAVITY = 0.8
PLAYER_JUMP = 15.5

# Image
charL1 = "charL1.png" # character 왼쪽 이동시 움직임1
charL2 = "charL2.png" # character 왼쪽 이동시 움직임2
charL3 = "charL3.png" # character 왼쪽 이동시 움직임3
tutMapBig = "tutMapBig.PNG" # tutorial map big block
tutMapStop = "tutMapStop.PNG" # tutorial map small block(위쪽이 검은색)
tutMapS = "tutMapS.PNG" # only small red block
s1MapBig = "s1MapBig.PNG"
s1MapStop = "s1MapStop.PNG"
s1MapS = "s1MapS.PNG"
s2MapBig = "s2MapBig.PNG"
s2MapStop = "s2MapStop.PNG"
s2MapS = "s2MapS.PNG"

YELLOW_BUBBLE = "./image/yellow_bubble.png"
PINK_BUBBLE = "./image/pink_bubble.png"
YELLOW_SUPERBUBBLE = "./image/yellow_superbubble.png"
PINK_SUPERBUBBLE = "./image/pink_superbubble.png"
START_SCREEND = "./image/start.png"
ENDING_IMAGE = "./image/end.png"


# about map
mapFile = ["map/tut_map.txt", "map/stage1_map.txt"]
mapTxt = [("q", "a", "z"), ("q", "a", "z")] # (big, small_top, small_bottom, shadow)
mapImage = [(tutMapBig, tutMapStop, tutMapS), (s1MapBig, s1MapStop, s1MapS)] # (big, small_top, small_bottom)
PLATFORM_LIST = [(0,70,TILESIZE, TILESIZE), (0,140, TILESIZE, TILESIZE), (70*14,140, TILESIZE, TILESIZE), (70, 675, 70, 25),
                 (70*3, 70*8, 70, 25), (70*3, 70*6+25, 70, 25), (70*10, 70*4+35, 70, 25)] # tutorial map
PLATFORM1_LIST = [(0,70,TILESIZE, TILESIZE), (0,140, TILESIZE, TILESIZE), (70*14,140, TILESIZE, TILESIZE), (70, 675, 70, 25),
                 (70, 70*8, 70, 25), (70, 70*6+25, 70, 25), (70, 70*4+35, 70, 25)] # stage1 map
PLATFORM2_LIST = [(0,70,TILESIZE, TILESIZE), (0,140, TILESIZE, TILESIZE), (70*14,140, TILESIZE, TILESIZE), (70, 675, 70, 25),
                 (70, 70*9-45, 70, 25), (70, 70*7-35, 70, 25), (70, 70*5, 70, 25), (70, 70*4-35, 70, 25)] # stage1 map