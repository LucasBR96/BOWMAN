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

DEFAULT_X   = 0
BOW_HEIGHT  = 1.7

#Field ----------------------------------------------------
FIELD_LEN = 400
BOW_MAN_DIST = 250
WIND_SPEED   = 0
MAX_WSP      = 100

#----------------------------------------------------------
# Conversao de distancias
R = 100 #pixels por metro

#-----------------------------------------------------------
# Cores

BLACK = ( 0 , 0 , 0 )
WHITE = ( 255 , 255 , 255 )