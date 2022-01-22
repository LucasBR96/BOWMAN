import numpy
import functools
from collections import namedtuple

import pygame
from pygame.locals import *
from constantes import *

ms = pygame.mouse

class BowmanSprite:

    def __init__( self , window ,left_side = True ):

        self.left_side = left_side
        self.window = window

        self.position = SCREEN_SIZE[ 0 ]//2

        self.drag = None
        self.conv = None
    
    def set_conv( self, conv ):
        self.conv = conv
        
    def set_drag( self , drag ):
        self.drag = drag

    def draw( self ):

        img_name = self.get_correct_sprite( )
        sprite = pygame.image.load( img_name )
        if self.should_flip():
            sprite = pygame.transform.flip( sprite , True , False )

        box = sprite.get_rect()
        sprite_x = self.position - box.width/2
        sprite_y = SCREEN_SIZE[ 1 ] - box.height - 10

        self.window.blit( sprite , ( sprite_x , sprite_y ) )

    def should_flip( self ):

        a = self.left_side
        b = self.drag.last_click is None

        if ( not a ) and b:
            return True
        
        elif b:
            return False
    
        x1 , _ = self.drag.last_click
        x2 , _ = ms.get_pos( )
        return x1 < x2
        
    def point_up( self ):

        if self.drag.last_click is None:
            return False

        x1 , y1 = self.drag.last_click
        x2 , y2 = ms.get_pos( )
        h = ( x1 - x2 )
        v = ( y1 - y2 )

        return ( v < 0 ) and ( abs( h ) < abs( v ) ) 

    def get_correct_sprite( self ):

        if ( self.drag.last_click is None ):
            return 'assets/bowman_sprites/Resting.png'

        _ , _ , d , _ = self.drag.get_drag_info()
        pull_idx = min( d//25 + 1 , 4 )
        
        theta_idx = self.point_up()

        return 'assets/bowman_sprites/Pull_{}{}.png'.format( int( theta_idx ) , int( pull_idx ) )

    def set_bow_params( self ):

        _ , _ , d , theta = self.drag.get_drag_info()
        self.bow.setTheta( theta )
        self.bow.setPull( d )
    


# class Bowman:

#     def __init__( self , Position ):

#         self.HP = MAX_HEALTH
#         self.Stamina = MAX_STAMINA

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


