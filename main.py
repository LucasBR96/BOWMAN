
from CLASSES.arrow import *
from CLASSES.bow import *
from CLASSES.bowman import *
from CLASSES.constantes import *
from CLASSES.conv import *

from SCREENS.constantes import *
from SCREENS.menu import Menu
from SCREENS.play import Play
from SCREENS.options import Options

import numpy as np

import pygame
pygame.init()
pygame.font.init()
from pygame.locals import *


def init_globals():

    global window
    window = pygame.display.set_mode( size = SCREEN_SIZE )

    global screen
    screen = Menu

    # global mouse
    # mouse = pygame.mouse

    global Font
    Font = pygame.font.SysFont( FONT_TYPE , FONT_SIZE , bold = True )

def swap_screen():

    global screen
    if screen.next_screen == VS_PLAY or screen.next_screen == VS_COMP:
        screen = Play
    
    elif screen.next_screen == OPT:
        screen = Options
    
    screen.start()


def main():

    init_globals()
    screen.start()
    while True:

        window.fill( WHITE )

        if screen.running:
            screen.render_objects( window , font = Font )
            screen.manage_inputs()
        else:
            swap_screen()

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()

        pygame.display.update()

if __name__ == "__main__":
    main()