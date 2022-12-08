import pathlib
from game.casting.color import Color
from game.casting.point import Point
# --------------------------------------------------------------------------------------------------
# GENERAL GAME CONSTANTS
# --------------------------------------------------------------------------------------------------

# GAME
GAME_NAME = "PONG"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "batter/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "batter/assets/sounds/boing.wav"
WELCOME_SOUND = "batter/assets/sounds/start.wav"
OVER_SOUND = "batter/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4


# --------------------------------------------------------------------------------------------------
# SCRIPTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# --------------------------------------------------------------------------------------------------
# CASTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# STATS
STATS_GROUP = "stats"
# DEFAULT_LIVES = 3
# MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
# LEVEL_GROUP = "level"
# LIVES_GROUP = "lives"
SCORE_GROUP = "score"
# LEVEL_FORMAT = "LEVEL: {}"
# LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"
SCORE_1_POSITION = Point(100,HUD_MARGIN)
SCORE_2_POSITION = Point(SCREEN_HEIGHT-20,HUD_MARGIN)

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "batter/assets/images/000.png"
BALL_WIDTH = 20
BALL_HEIGHT = 20
BALL_VELOCITY = 9

# RACKET
RACKET_GROUP = "rackets"
RACKET_IMAGES = [f"batter/assets/images/{n:03}.png" for n in range(100, 103)]
RACKET_WIDTH = 106
RACKET_HEIGHT = 28
RACKET_RATE = 6
RACKET_VELOCITY = 10


# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"

PLAYER1_SLOT = 0
PLAYER2_SLOT = 1
PLAYER1_NAME = "Player1"
PLAYER2_NAME = "Player2"

PLAYER1_LEFT = "a"
PLAYER1_RIGHT = 'd'

PLAYER2_LEFT = "left"
PLAYER2_RIGHT = "right"

PLAYER_SCORE_INC = 1