import numpy
from CLASSES.arrow import Arrow
from UTILS.clock import Clock
from UTILS.conv import Conv
from UTILS.camera import camera

import pygame
from pygame.locals import *

from constantes import BLACK, SCREEN_SIZE

class ArrowList:

    def __init__( self , window ):

        self.lst : list[ Arrow ] = []
        self.window = window

        self.conv : Conv = None
        self.clock : Clock = None
        self.camera : camera = None

        self.init_arrow_sprites()
    
    def init_arrow_sprites( self ):

        self.arrow_sprites = []
        img = pygame.image.load( "assets/arrow_sprites/arrow1.png" )
        for i in range( 91 ):

            if i == 0:
                aux = img
            else:
                aux = pygame.transform.rotate( img , i )
            rect = aux.get_rect()
            self.arrow_sprites.append( ( aux , rect ) )
    
    def get_correct_sprite( self , x ):

        m = int( numpy.floor( x ) )
        return self.arrow_sprites[ m ]

    
    def set_conv( self, conv : Conv ):
        self.conv = conv

    def set_clock( self , clock ):
        self.clock = clock
    
    def set_camera( self , camera ):
        self.camera = camera

    def add_arrow( self , arr : Arrow ):

        # self.camera.focus_at( arr )
        self.lst.append( arr )
    
    def move_arrow( self ):

        dt = self.clock.last_dt
        for arrow in self.lst:
            if arrow.Flying:
                arrow.Fly( dt )
                arrow.Accelerate( dt )
                arrow.Lock()
    
    def draw( self ):

        focus = self.camera.get_focus()
        if focus is None:
            return
            
        focus = self.conv.fromVirt( focus[ 0 ] , focus[ 1 ] )
        dx = focus[ 0 ] - SCREEN_SIZE[ 0 ]/2
        dy = focus[ 1 ] - SCREEN_SIZE[ 1 ]/2

        for arrow in self.lst:

            p = arrow.Center
            p = self.conv.fromVirt( p[0] , p[ 1 ])
            p = ( p[0] - dx , p[1] - dy )

            #Alinhado a flecha com a velocidade -----------------------------
            vx , vy = arrow.Speed
            theta = numpy.rad2deg( numpy.arctan( vy/vx ) )
            img , rect = self.get_correct_sprite( abs( theta ) )
            a = ( vx < 0 )
            b = ( vy < 0 )
            img = pygame.transform.flip( img , a , b )

            #centralizando o sprite com o centro da flecha -------------------
            w = rect.width/2
            h = rect.height/2
            p -= numpy.array( [ w , h ] )

            pygame.draw.rect( self.window , BLACK , ( p[0] , p[ 1 ] , 2*w , 2*h ) , width = 1  )
            self.window.blit( img , p )
            
    
    def update( self ):

        self.move_arrow()


        