
#title
TITLE = "game"

#FPS
FPS = 60
frame_count = 0
start_time = 90

#font
font_name = "Arial"

#player properties
PLAYER_ACC = 0.8
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8

#enemy properties
ENEMY_ACC = 0.5
ENEMY_FRICTION = -0.12
ENEMY_GRAV = 0.8

#level map
level_map = [
"                                 ",
"          E                      ",
"       xxxxxxxx                  ",
"                  xxxxxx         ",
"                xx               ",
"                          xxxxxxx",
"    xxxxx  x  xxx    xxxxxxxxxxxx",
"xxx             x                ",
"    xx                           ",
" xxxxxxxxxxxxx  xx               ",
" xxxxxxxxxxxxx       xxxxxxxxxxxx",
"                xx               ",
"  P                               ",
"xxxxxxxxxxxxxxxxx    xxxxxxxxxxxx"]
tile_size = 50

#screen size
width = 1300
height = len(level_map) * tile_size


#library of colours
BLACK = ( 0, 0, 0)
WHITE = (225, 225, 225)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
Peach = (255, 204, 153)
BROWN = (204, 102, 0)
SKY = (102, 178, 255)
YELLOW = (225, 255, 0)
GLASS = (204, 255, 255)
X = (173, 26, 168)
TEAL = (3, 252, 194)
