import numpy
import functools
from collections import namedtuple

from pygame import sprite

from SCREENS.constantes import *

import pygame
from pygame.locals import *

ms = pygame.mouse

class Bowman:

    def __init__( self , window ,left_side = True ):

        self.left_side = left_side
        self.window = window

        self.position = SCREEN_SIZE[ 0 ]//2

        self.drag = None
    
    def draw( self ):

        img_name = self.get_correct_sprite( )
        sprite = pygame.image.load( img_name )
        if self.should_flip():
            sprite = pygame.transform.flip( sprite , True , False )

        box = sprite.get_rect()
        sprite_x = self.position - box.width/2
        sprite_y = SCREEN_SIZE[ 1 ] - box.height - 10

        self.window.blit( sprite , ( sprite_x , sprite_y ) )

    def set_drag( self , drag ):
        self.drag = drag
    
    def should_flip( self ):

        a = self.left_side
        b = self.drag.last_click is None

        if ( not a ) and b:
            return True

        if b:
            return False
        
        x1 , _ = self.drag.last_click
        x2 , _ = ms.get_pos( )

        c = x1 > x2
        if a and not c:
            return True

        return False
        
    def get_correct_sprite( self ):

        if ( self.drag.last_click is None ):
            return 'assets/bowman_sprites/Resting.png'

        _ , _ , d , theta = self.drag.get_drag_info()
        

        pull_idx = min( d//25 + 1 , 4 )
        
        theta_idx = 0
        if theta > numpy.pi/4:
            theta_idx = 1

        return 'assets/bowman_sprites/Pull_{}{}.png'.format( int( theta_idx ) , int( pull_idx ) )
    
        # self.HP = MAX_HEALTH
        # self.Stamina = MAX_STAMINA

        # self.Bow         = Bow
        # self.Inventory   = Inventory
        # self.loadedArrow = list( Inventory.keys() )[ 0 ]

        # self.Position = Position
    
    # def Draw( self , Pull , Theta ):

    #     self.Bow.setTheta( Theta )
    #     self.Bow.setPull( Pull )
    
    # def updateStamina( self , dt ):
        
    #     x = self.Bow.Pull
    #     if x != 0:
    #         return self.getTired( dt )
    #     return self.getRest( dt )
    
    # def getRest( self , dt ):
    #     self.Stamina = MAX_STAMINA
    #     return False

    # def getTired( self , dt ):

    #     Bow = self.Bow
    #     x = Bow.Pull
    #     k = Bow.Power
    #     d = Bow.WetDebuff
    #     Force = x*k*d

    #     self.Stamina -= Force*dt*STAMINA_DECAY
    #     self.Stamina  = max( self.Stamina , 0 )
    #     return self.Stamina == 0 
    
    # def Loose( self ) -> Arrow:

    #     ArrowType = self.loadedArrow
    #     Position  = numpy.array([ self.Position , BOW_HEIGHT ] )
    #     newArrow  = self.Bow.Loose( ArrowType , Position )

    #     self.Inventory[ ArrowType ] -= 1
    #     self.Bow.setPull( 0 )

    #     return newArrow


