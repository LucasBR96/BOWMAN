from SCREENS.constantes import *

import pygame
from pygame.locals import *

class Options:

    @staticmethod
    def start():
        
        Options.running = True
        Options.next_screen = None

    @staticmethod
    def render_objects( window , **kwargs ):
        pass

    @staticmethod
    def manage_inputs(  ):
        pass