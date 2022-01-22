from constantes import *

import pygame
from pygame.locals import *

from numpy import sqrt , arctan, pi, rad2deg

ms = pygame.mouse
class mouse_drag:

    def __init__( self , window ):

        self.window = window
        self.last_click = None
        self.font = pygame.font.SysFont( FONT_TYPE , DRAG_FONT_SIZE , bold = True )
    
    def update_drag( self , p1 , p2 , d ):

        r = MAX_DRAG_D/d
        dx = r*( p1[0] - p2[0] )
        dy = r*( p1[1] - p2[1] )

        new_x = p1[0] - dx
        new_y = p1[1] - dy

        return ( new_x , new_y )

    def get_drag_info( self ):

        p1 = self.last_click
        p2 = ms.get_pos()

        ( x1 , y1 ) , ( x2 , y2 ) = p1 , p2
        d = sqrt( ( x1 - x2 )**2 + ( y1 - y2 )**2 )
        if d > MAX_DRAG_D:
            p2 = self.update_drag( p1 , p2 , d )
            x2 , y2 = p2
            d = MAX_DRAG_D

        try:
            a = ( y1 >= y2 )
            b = ( x1 >= x2 )

            if a and b:
                r = ( y1 - y2 )/( x1 - x2 )
            
            elif a:
                r = ( y1 - y2 )/( x2 - x1 )
            
            elif b:
                r = ( y2 - y1 )/( x1 - x2 )
            
            else:
                r = ( y2 - y1 )/( x1 - x2 )
            
            theta = arctan( r )
            # theta = arctan( ( y1 - y2 )/( x2 - x1 ) )
        except ZeroDivisionError:
            theta = pi/2

        return p1 , p2 , d/2 , theta

    def update( self ):

        if ms.get_pressed()[ 0 ] and self.last_click is None:
            self.last_click = ms.get_pos()
        elif not( ms.get_pressed()[ 0 ] ) and not( self.last_click is None ):
            self.last_click = None

    def draw( self ):

        if self.last_click is None:
            return

        p1 , p2 , d , theta = self.get_drag_info()
        window = self.window

        pygame.draw.line( window , BLACK , p1 , p2 , width = DRAG_LINE_THICKNESS )

        font = self.font

        s1 = "{:.2f}".format( d )
        text = font.render( s1 , False, BLACK)
        window.blit( text , ( DRAG_TEXT_X , DRAG_TEXT_Y ) )

        w = text.get_rect().width
        s2 = "{:.2f}".format( rad2deg( theta ) )
        text = font.render( s2 , False, BLACK)
        window.blit( text , ( DRAG_TEXT_X + w + 10, DRAG_TEXT_Y ) )     



        