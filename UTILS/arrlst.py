import numpy
from CLASSES.arrow import Arrow
from UTILS.clock import Clock
from UTILS.conv import Conv
from UTILS.camera import camera

import pygame
from pygame.locals import *

from constantes import BLACK

class ArrowList:

    def __init__( self , window ):

        self.lst : list[ Arrow ] = []
        self.window = window

        self.conv : Conv = None
        self.clock : Clock = None
        self.camera : camera = None
    
    def set_conv( self, conv : Conv ):
        self.conv = conv

    def set_clock( self , clock ):
        self.clock = clock
    
    def set_camera( self , camera ):
        self.camera = camera

    def add_arrow( self , arr : Arrow ):

        self.camera.focus_at( arr )
        self.lst.append( arr )
    
    def move_arrow( self ):

        dt = self.clock.last_dt
        for arrow in self.lst:
            if arrow.Flying:
                arrow.Fly( dt )
                arrow.Accelerate( dt )
                arrow.Lock()
    
    def draw( self ):

        img = pygame.image.load( "assets/arrow_sprites/arrow1.png" )
        for arrow in self.lst:

            p1 , p2 = arrow.GetEdges()
            # focus = self.camera.get_focus()

            # p1 -= focus
            p1 = self.conv.fromVirt( p1[0] , p1[1] )

            # p2 -= focus
            p2 = self.conv.fromVirt( p2[0] , p2[1] )

            pygame.draw.line( self.window , BLACK , p1 , p2 )

            p = arrow.Center
            p = self.conv.fromVirt( p[0] , p[ 1 ])

            #centralizando o sprite com o centro da flecha -------------------
            w = img.get_rect().width/2
            h = img.get_rect().height/2
            p -= numpy.array( [ w , h ] )

            #Alinhado a flecha com a velocidade -----------------------------
            ( x1 , y1 ) , ( x2 , y2 ) = p1 , p2
            try:
                theta = numpy.arctan( ( y1 - y2 )/( x1 - x2 ) )
                if ( x2 > x1 ):
                    theta += numpy.pi
            except ZeroDivisionError:
                theta = numpy.pi/2

            img = pygame.transform.rotate( img , numpy.rad2deg( theta ) )

            self.window.blit( img , p )
            
    
    def update( self ):

        self.move_arrow()


        