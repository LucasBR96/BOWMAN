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
        Play.left_bow.draw()
        Play.right_bow.draw()
        Play.arrlst.draw()
        pass
    
    @staticmethod
    def update( ):

        Play.clock.tick()
        Play.set_focus()
        Play.right_bow.update()
        Play.left_bow.update()
        Play.arrlst.update()
        
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
        
