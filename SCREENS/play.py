from constantes import *
from UTILS.drag import mouse_drag
from UTILS.bowman import BowmanSprite
from UTILS.conv import Conv
from UTILS.arrlst import ArrowList
from UTILS.clock import Clock
from UTILS.camera import camera

import pygame
from pygame.locals import *

from numpy import sqrt , arctan, pi, rad2deg

import time
kb = pygame.key
ms = pygame.mouse 
class Play:

    @staticmethod
    def start( window ):

        time.sleep( .1 )
        Play.running = True
        Play.next_screen = None

        Play.window = window
        Play.drag   = mouse_drag( window )
        Play.clock = Clock()
        Play.conv  = Conv()
        Play.camera = camera()
        
        Play.arrlst = ArrowList( window )
        Play.arrlst.set_clock( Play.clock )
        Play.arrlst.set_conv( Play.conv )
        Play.arrlst.set_camera( Play.camera )

        Play.left_bow = BowmanSprite( window )
        Play.left_bow.set_drag( Play.drag )
        Play.left_bow.set_conv( Play.conv )
        Play.left_bow.set_arrowlst( Play.arrlst )
        Play.left_bow.set_camera( Play.camera )

        Play.right_bow = BowmanSprite( window , left_side = False)
        Play.right_bow.set_drag( Play.drag )
        Play.right_bow.set_conv( Play.conv )
        Play.right_bow.set_arrowlst( Play.arrlst )
        Play.right_bow.set_camera( Play.camera )

    @staticmethod
    def switch_turn( ):

        right_bow = Play.right_bow
        left_bow  = Play.left_bow
        for bow in [ right_bow , left_bow ]:
            bow.turn = not bow.turn
        
    @staticmethod
    def set_focus( ):

        cmra = Play.camera
        if cmra.focus is None:
            cmra.focus_at( Play.left_bow.bowman )
            return
        
        try:
            arr  = Play.arrlst.lst[ -1 ]
        except IndexError:
            return

        if arr.Flying and cmra.focus == arr:
            return
        
        if ( not arr.Flying ) and ( cmra.focus != arr ):
            return
        
        if arr.Flying:
            cmra.focus_at( arr )
            return
        
        Play.switch_turn()
        right_bow = Play.right_bow
        left_bow  = Play.left_bow
        bow = right_bow if right_bow.turn else left_bow

        cmra.focus_at( bow.bowman )


    @staticmethod
    def render_objects( window , **kwargs ):

        Play.drag.draw()
        Play.arrlst.draw()
        Play.left_bow.draw()
        Play.right_bow.draw()

        Play.draw_floor()
        Play.draw_hp()
        pass
    
    @staticmethod
    def check_for_hit( ):

        right_bow = Play.right_bow
        left_bow  = Play.left_bow
        target = right_bow if left_bow.turn else left_bow
        Play.arrlst.check_for_hit( target )
    
    @staticmethod
    def draw_floor():

        cmr = Play.camera
        focus = cmr.get_focus()

        try:
            _ , fy = Play.conv.fromVirt( focus[ 0 ] , focus[ 1 ] )

            dy = fy - SCREEN_SIZE[ 1 ]/2
            p1 = ( 0 ,SCREEN_SIZE[ 1 ] - FLOOR_HEIGHT - dy )
            p2 = ( SCREEN_SIZE[ 0 ] ,SCREEN_SIZE[ 1 ] - FLOOR_HEIGHT - dy )

        except TypeError:
            p1 = ( 0 ,SCREEN_SIZE[ 1 ] - FLOOR_HEIGHT )
            p2 = ( SCREEN_SIZE[ 0 ] , SCREEN_SIZE[ 1 ] - FLOOR_HEIGHT )

        pygame.draw.line( Play.window , BLACK , p1 , p2 , width = 4 )  

    @staticmethod
    def draw_hp():

        font = pygame.font.SysFont( FONT_TYPE , 16, bold = True )
        left_hp = Play.left_bow.bowman.HP
        right_hp = Play.right_bow.bowman.HP

        box1 = font.render( "HP1 = {}".format( left_hp ) , False , BLACK )
        h = box1.get_rect().height
        Play.window.blit( box1 , ( 0 , SCREEN_SIZE[ 1 ]//2  + h ))

        box2 = font.render( "HP2 = {}".format( right_hp ) , False , BLACK )
        Play.window.blit( box2 , ( 0 , SCREEN_SIZE[ 1 ]//2 ))

    @staticmethod
    def update( ):

        Play.clock.tick()
        Play.set_focus()

        Play.right_bow.update()
        Play.left_bow.update()
        Play.arrlst.update()
        
        Play.check_for_hit()
        if ms.get_pressed()[ 0 ]:

            x1 , x2 = ms.get_pos()
            v1 , v2 = Play.conv.toVirt( x1 , x2 )

            print( f'Pixel: {x1} {x2}')
            print( f'Virtual: {v1} {v2}')

    @staticmethod
    def manage_inputs(  ):
        
        if kb.get_pressed()[ K_ESCAPE ]:
            Play.running = False
            Play.next_screen = MENU
        
        if kb.get_pressed()[ K_SPACE ]:
            Play.running = not Play.running

        Play.drag.update()
        
