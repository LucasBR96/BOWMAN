import numpy

#Arrow -------------------------------------------------
BASE_MASS = .3
BASE_LEN  = 1


#Bow   -------------------------------------------------
MIN_THETA = 0.
MAX_THETA = numpy.pi/2

MAX_PULL  = 1.
WET_DEBUFF = .2
MAX_WET_DEBUFF = .8
MIN_WET_DEBUFF = .1

#Bowman --------------------------------------------------

MAX_HEALTH  = 100
MAX_STAMINA = 100
STAMINA_DECAY = 5/MAX_STAMINA

VIRTUAL_DEFAULT_X   = 75
VIRTUAL_BOW_HEIGHT  = 1.5
VIRTUAL_BOWMAN_HEIGHT  = 1.7

#Field ----------------------------------------------------
FIELD_LEN = 400
BOW_MAN_DIST = 250
WIND_SPEED   = 0
MAX_WSP      = 100

#----------------------------------------------------------
# Conversao de distancias
R = 54 #pixels por metro
FLOOR_HEIGHT = 10
CENTER = numpy.array( [ -66*R , 800 - FLOOR_HEIGHT ] )
MAT = numpy.array( [ [ R , 0 ] , [ 0 , -R ] ] )

#--------------------------------------------------------
# Opcoes gerais
SCREEN_SIZE = ( 1200 , 800 )
WHITE       = ( 255 , 255 , 255 )
BLACK       = ( 0 , 0 , 0 )

#-------------------------------------------------------
# Menu
VS_PLAY , VS_COMP , OPT , EXIT = range( 4 )
MENU = 4

BUTTON_W = 200
BUTTON_H = 70
W_GAP    = 80

VS_PLAY_POS = ( ( SCREEN_SIZE[ 0 ] - 4*BUTTON_W - 3*W_GAP )/2 , ( SCREEN_SIZE[ 1 ] - BUTTON_H )/2 )
VS_COMP_POS = ( VS_PLAY_POS[ 0 ] + BUTTON_W + W_GAP , VS_PLAY_POS[ 1 ] )
OPT_POS = ( VS_COMP_POS[ 0 ] + BUTTON_W + W_GAP , VS_PLAY_POS[ 1 ] )
EXIT_POS = ( OPT_POS[ 0 ] + BUTTON_W + W_GAP , VS_PLAY_POS[ 1 ] )

BUTTON_THICKNESS = 3

FONT_TYPE = 'lato'
FONT_SIZE = 18

#-----------------------------------------------------------
# Arrow drag
DRAG_LINE_THICKNESS = 3 
DRAG_FONT_SIZE      = 12
DRAG_TEXT_X         = 0
DRAG_TEXT_Y         = 3

MAX_DRAG_D = 200