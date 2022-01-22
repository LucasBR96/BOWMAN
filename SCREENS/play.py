from constantes import *
from UTILS.drag import mouse_drag
from UTILS.bowman import BowmanSprite
from UTILS.conv import Conv

import pygame
from pygame.locals import *

from numpy import sqrt , arctan, pi, rad2deg

class Play:

    @staticmethod
    def start( window ):

        Play.running = True
        Play.next_screen = None

        Play.drag = mouse_drag( window )
        Play.conv = Conv()
        Play.left_bow = BowmanSprite( window )
        Play.left_bow.set_drag( Play.drag )
        Play.left_bow.set_conv( Play.conv )
        pass

    @staticmethod
    def render_objects( window , **kwargs ):
        Play.drag.draw()
        Play.left_bow.draw()
        pass

    @staticmethod
    def manage_inputs(  ):
        
        kb = pygame.key
        if kb.get_pressed()[ K_ESCAPE ]:
            Play.running = False
            Play.next_screen = MENU
        
        if kb.get_pressed()[ K_SPACE ]:
            Play.running = not Play.running

        Play.drag.update()
        
