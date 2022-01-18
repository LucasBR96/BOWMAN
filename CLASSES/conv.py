import numpy
from numpy import linalg

import functools
from collections import namedtuple

from CLASSES.constantes import *

class Conv:

    def __init__( self , Center , Mat ):

        self.Center = Center
        self.Mat    = Mat

        self.Inv = linalg.inv( Mat )
    
    def toVirt( self, RealX , RealY ):

        P   = numpy.array( [ RealX , RealY ] )
        C   = self.Center
        Inv = self.Inv

        return ( P - C )@Inv
    
    def fromVirt( self , VirtualX , VirtualY ):

        K   = numpy.array( [ VirtualX , VirtualY ] )
        C   = self.Center
        Mat = self.Mat

        return C + K@Mat