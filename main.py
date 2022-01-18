from turtle import screensize
from CLASSES.arrow import *
from CLASSES.bow import *
from CLASSES.bowman import *
from CLASSES.constantes import *
from CLASSES.conv import *

from SCREENS.constantes import *
from SCREENS.menu import Menu

import numpy as np

import pygame
from pygame.locals import *

def init_globals():

    global window
    window = pygame.display.set_mode( size = SCREEN_SIZE )

    global screen
    screen = Menu

def main():
    
    init_globals()
    while True:

        window.fill( WHITE )
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()

if __name__ == "__main__":
    main()