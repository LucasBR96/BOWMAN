
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

#----------------------------------------------------------
# Conversao de distancias

#-----------------------------------------------------------
# Arrow drag
DRAG_LINE_THICKNESS = 3 
DRAG_FONT_SIZE      = 12
DRAG_TEXT_X         = 0
DRAG_TEXT_Y         = 3