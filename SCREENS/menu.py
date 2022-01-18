from SCREENS.constantes import *

import pygame
from pygame.locals

class Menu:

    @staticmethod
    def start():
        
        opt_types = [ VS_PLAY , VS_COMP , OPT , EXIT ]

        Menu.buttons = { x:dict() for x in opt_types }

        Menu.buttons[ VS_PLAY ] = pygame.rect.Rect( VS_PLAY_POS , ( BUTTON_W , BUTTON_H ) )
        # Menu.buttons[ VS_PLAY ] = pygame.rect.Rect( VS_PLAY_POS , ( BUTTON_W , BUTTON_H ) )

        Menu.buttons[ VS_COMP ] = pygame.rect.Rect( VS_COMP_POS , ( BUTTON_W , BUTTON_H ) )
        # Menu.buttons[ VS_COMP ] = pygame.rect.Rect( )

        Menu.buttons[ OPT ] = pygame.rect.Rect( OPT_POS , ( BUTTON_W , BUTTON_H ) )
        # Menu.buttons[ OPT ][ HVR ].set_position( *RANK_POS )

        Menu.buttons[ EXIT ]= pygame.rect.Rect( EXIT_POS , ( BUTTON_W , BUTTON_H ) )
        # Menu.buttons[ EXIT ][ HVR ].set_position( *EXIT_POS )

        Menu.selected = [0]*4
        Menu.running = True
        Menu.next_screen = None
