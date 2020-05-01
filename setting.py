#base properties
TITLE = "Bubble Bobble"
WIDTH = 1050
HEIGHT = 700
FPS = 60

TILESIZE = 70

#Font
#Player properties

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
keys = [False, False, False, False, False]

# about character
char_pos = [70, 630]

# Image
charL1 = "charL1.png" # character 왼쪽 이동시 움직임1
charL2 = "charL2.png" # character 왼쪽 이동시 움직임2
charL3 = "charL3.png" # character 왼쪽 이동시 움직임3
tutMapBig = "tutMapBig.PNG" # tutorial map big block
tutMapSbot = "tutMapSbot.PNG" # tutorial map small block(아래쪽이 검은색)
tutMapStop = "tutMapStop.PNG" # tutorial map small block(위쪽이 검은색)
tutMapS = "tutMapS.PNG" # only small red block
s1MapBig = "s1MapBig.PNG"
s1MapStop = "s1MapStop.PNG"
s1MapSbot = "s1MapSbot.PNG"

# about map
mapFile = ["map/tut_map.txt", "map/stage1_map.txt"]
mapTxt = [("q", "a", "z"), ("q", "a", "z")] # (big, small_top, small_bottom, shadow)
mapImage = [(tutMapBig, tutMapStop, tutMapS), (s1MapBig, s1MapStop, s1MapSbot)] # (big, small_top, small_bottom)