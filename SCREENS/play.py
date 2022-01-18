from SCREENS.constantes import *

import pygame
from pygame.locals import *

class Play:

    @staticmethod
    def start():

        Play.running = True
        Play.next_screen = None
        pass

    @staticmethod
    def render_objects( window , **kwargs ):
        pass

    @staticmethod
    def manage_inputs(  ):
        pass
