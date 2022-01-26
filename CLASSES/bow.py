import numpy
import functools
from collections import namedtuple

from CLASSES.arrow import Arrow, ArrowProfile
from constantes import *

class Bow:

    def __init__( self , Power = 2*10**3 , MaxPull = MAX_PULL, WetDebuff = WET_DEBUFF ):

        self.Power     : float = Power
        self.Theta     : float = 0
        self.Pull      : float = 0
        self.MaxPull   : float = MaxPull
        self.WetDebuff : float = WetDebuff
        pass

    def getReleaseVelocity( self ):

        d = self.WetDebuff
        k = self.Power
        x = self.Pull
        Energy = ( 1 - d )*( k*( x**2 ) )

        # m = ArrType.Mass
        m = BASE_MASS
        Velocity = Energy/m

        return numpy.sqrt( Velocity )

    def Loose( self , Center ) -> Arrow:

        Velocity = self.getReleaseVelocity( )

        Theta    = self.Theta
        cosTheta = numpy.cos( Theta )
        sinTheta = numpy.sin( Theta )

        Speed = numpy.array( [ cosTheta , sinTheta ] )*Velocity
        return Arrow(  Center , Speed  )

    def setTheta( self , Theta ):
        self.Theta = Theta

    def setPull( self , Pull : float ):
        self.Pull = Pull

