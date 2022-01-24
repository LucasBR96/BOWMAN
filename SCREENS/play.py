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
        pass

    @staticmethod
    def render_objects( window , **kwargs ):

        Play.drag.draw()
        Play.left_bow.draw()
        Play.arrlst.draw()
        pass
    
    @staticmethod
    def update( ):

        Play.clock.tick()
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
        
