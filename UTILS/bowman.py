
import numpy
import functools
from collections import namedtuple

import pygame
from pygame.locals import *
from constantes import *

from CLASSES.bowman import Bowman

# from UTILS.arrlst import arrlst:

ms = pygame.mouse
class BowmanSprite:

    def __init__( self , window ,left_side = True ):

        self.left_side = left_side
        self.window = window

        if self.left_side:
            self.position = SCREEN_SIZE[ 0 ]//2
            self.bowman = Bowman()
        else:
            self.position =   SCREEN_SIZE[ 0 ]//2 + 250*R
            self.bowman = Bowman( Position = numpy.array([ VIRTUAL_DEFAULT_X + 250 , 0 ]))

        self.drag     = None
        self.conv     = None
        self.arrowlst = None
        self.camera   = None

        self.turn = left_side

    
    def set_conv( self, conv ):
        self.conv = conv

    def set_drag( self , drag ):
        self.drag = drag

    def set_camera( self , camera ):
        self.camera = camera

    def set_arrowlst( self , arrowlst ):
        self.arrowlst = arrowlst

    def draw( self ):

        img_name = self.get_correct_sprite( )
        sprite = pygame.image.load( img_name )
        if self.should_flip():
            sprite = pygame.transform.flip( sprite , True , False )

        box = sprite.get_rect()
        sprite_x = self.position - box.width/2
        sprite_y = SCREEN_SIZE[ 1 ] - box.height - FLOOR_HEIGHT

        try:
            focus = self.camera.get_focus()
            focus = self.conv.fromVirt( focus[ 0 ] , focus[ 1 ] )
            dx = focus[ 0 ] - SCREEN_SIZE[ 0 ]/2
            dy = focus[ 1 ] - SCREEN_SIZE[ 1 ]/2
        except TypeError:
            dx , dy = 0 , 0 

        self.window.blit( sprite , ( sprite_x - dx , sprite_y - dy  ) )

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

        if self.drag.last_click is None:
            return 'assets/bowman_sprites/Resting.png'

        _ , _ , d , _ = self.drag.get_drag_info()
        pull_idx = min( d//25 + 1 , 4 )
        
        theta_idx = self.point_up()

        return 'assets/bowman_sprites/Pull_{}{}.png'.format( int( theta_idx ) , int( pull_idx ) )

    def set_bow_params( self ):

        _ , _ , d , theta = self.drag.get_drag_info()
        self.bowman.Draw( d/100 , theta )
    
    def loose( self ):

        Arr = self.bowman.Loose()
        self.arrowlst.add_arrow( Arr )
    
    def update( self ):
        
        if self.turn:
            if self.drag.released():
                self.loose()
            elif self.drag.holding:
                self.set_bow_params()

        # try:
        #     arr = self.arrowlst.lst[ -1 ]
        #     if not arr.Flying:
        #         self.camera.focus_at( self.bowman )
        # except IndexError:
        #     return



