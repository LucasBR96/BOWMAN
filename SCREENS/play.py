from SCREENS.constantes import *
from SCREENS.drag import mouse_drag
from SCREENS.bowman import Bowman

import pygame
from pygame.locals import *

from numpy import sqrt , arctan, pi, rad2deg

class Play:

    @staticmethod
    def start( window ):

        Play.running = True
        Play.next_screen = None

        Play.drag = mouse_drag( window )
        Play.left_bow = Bowman( window )
        Play.left_bow.set_drag( Play.drag )
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
        
