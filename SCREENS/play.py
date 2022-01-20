
from sqlalchemy import false
from SCREENS.constantes import *

import pygame
from pygame.locals import *

from numpy import sqrt , arctan, pi, rad2deg

def handle_mouse_click( ):

    ms = pygame.mouse
    if ms.get_pressed()[ 0 ] and Play.last_player_click is None:
        Play.last_player_click = ms.get_pos()
        # print( Play.last_player_click )
    elif not( ms.get_pressed()[ 0 ] ) and not( Play.last_player_click is None ):
        Play.last_player_click = None

def get_drag_info():

    ms = pygame.mouse

    p1 = Play.last_player_click
    p2 = ms.get_pos()

    ( x1 , y1 ) , ( x2 , y2 ) = p1 , p2
    d = sqrt( ( x1 - x2 )**2 + ( y1 - y2 )**2 )

    try:
        theta = arctan( ( y1 - y2 )/( x2 - x1 ) )
    except ZeroDivisionError:
        theta = pi/2

    return p1 , p2 , d , theta

def draw_mouse_drag( window ):

    ms = pygame.mouse
    if not( ms.get_pressed()[ 0 ] ) or Play.last_player_click is None:
        return

    p1 , p2 , d , theta = get_drag_info()
    pygame.draw.line( window , BLACK , p1 , p2 , width = DRAG_LINE_THICKNESS )

    font = pygame.font.SysFont( FONT_TYPE , DRAG_FONT_SIZE , bold = True )
    
    s1 = "{:.2f}".format( d )
    text = font.render( s1 , False, BLACK)
    window.blit( text , ( DRAG_TEXT_X , DRAG_TEXT_Y ) )

    w = text.get_rect().width
    s2 = "{:.2f}".format( rad2deg( theta ) )
    text = font.render( s2 , False, BLACK)
    window.blit( text , ( DRAG_TEXT_X + w + 10, DRAG_TEXT_Y ) )

class Play:

    @staticmethod
    def start():

        Play.running = True
        Play.next_screen = None

        Play.last_player_click = None
        Play.current_mouse_pos = None
        pass

    @staticmethod
    def render_objects( window , **kwargs ):

        font = kwargs.get( 'font' )
        draw_mouse_drag( window )
        pass

    @staticmethod
    def manage_inputs(  ):
        
        kb = pygame.key
        if kb.get_pressed()[ K_ESCAPE ]:
            Play.running = False
            Play.next_screen = MENU
        
        handle_mouse_click()
        
