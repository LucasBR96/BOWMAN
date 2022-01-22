from constantes import *

import pygame
from pygame.locals import *


def render_buttons_text( window , font : pygame.font.SysFont ):

    for i , x in enumerate( Menu.selected ):

        color = BLACK if x else WHITE
        text : pygame.surface.Surface = font.render( Menu.texts[ i ] , True , color )

        butt_rect = Menu.buttons[ i ]
        text_rect = text.get_rect()
        center_x = butt_rect.centerx - text_rect.width/2
        center_y = butt_rect.centery - text_rect.height/2

        window.blit( text , ( center_x , center_y ) ) 

def handle_mouse_press():

    butt = None
    for i , x in enumerate( Menu.selected ):
        if x:
            butt = i
            break
    
    if butt is None:
        return
    
    if butt == EXIT:
        pygame.quit()

    Menu.running = False
    Menu.next_screen = butt

    pass
    
class Menu:

    @staticmethod
    def start( window ):
        
        opt_types = [ VS_PLAY , VS_COMP , OPT , EXIT ]

        Menu.buttons : list[ pygame.rect.Rect ] = []
        Menu.buttons.append( pygame.rect.Rect( VS_PLAY_POS , ( BUTTON_W , BUTTON_H ) ) )
        Menu.buttons.append( pygame.rect.Rect( VS_COMP_POS , ( BUTTON_W , BUTTON_H ) ) )
        Menu.buttons.append( pygame.rect.Rect( OPT_POS , ( BUTTON_W , BUTTON_H ) ) )
        Menu.buttons.append( pygame.rect.Rect( EXIT_POS , ( BUTTON_W , BUTTON_H ) ) )

        Menu.texts : list[ str ] = [ '' ]*4
        Menu.texts[ VS_PLAY ] = 'VS PLAYER'
        Menu.texts[ VS_COMP ] = 'VS COMPUTADOR'
        Menu.texts[ OPT ] = 'OPCOES'
        Menu.texts[ EXIT ] = 'SAIR'

        Menu.selected = [0]*4
        Menu.running = True
        Menu.next_screen = None

    @staticmethod
    def render_objects( window , **kwargs ):

        for i , x in enumerate( Menu.selected ):

            butt = Menu.buttons[ i ]
            pygame.draw.rect( window , BLACK , butt , width = x*BUTTON_THICKNESS  )

        Font = kwargs[ 'font' ]
        render_buttons_text( window , Font )

    @staticmethod
    def manage_inputs( ):

        mouse = pygame.mouse 
        x , y = mouse.get_pos()

        for i , button in enumerate( Menu.buttons ):
            Menu.selected[ i ] = int( button.collidepoint( x , y ) )
        
        if mouse.get_pressed()[ 0 ] == True:
            handle_mouse_press()