from CLASSES.arrow import Arrow
from UTILS.clock import Clock
from UTILS.conv import Conv

import pygame
from pygame.locals import *

from constantes import BLACK

class ArrowList:

    def __init__( self , window ):

        self.lst : list[ Arrow ] = []
        self.window = window

        self.conv : Conv = None
        self.clock : Clock = None
    
    def set_conv( self, conv : Conv ):
        self.conv = conv

    def set_clock( self , clock ):
        self.clock = clock

    def add_arrow( self , arr : Arrow ):
        self.lst.append( arr )
    
    def move_arrow( self ):

        dt = self.clock.last_dt
        for arrow in self.lst:
            if arrow.Flying:
                arrow.Fly( dt )
                arrow.Accelerate( dt )
    
    def draw( self ):

        for arrow in self.lst:

            p1 , p2 = arrow.GetEdges()
            p1 = self.conv.fromVirt( p1[0] , p1[1] )
            p2 = self.conv.fromVirt( p2[0] , p2[1] )

            pygame.draw.line( self.window , BLACK , p1 , p2 )
            
    
    def update( self ):

        self.move_arrow()


        