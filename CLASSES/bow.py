import numpy
import functools
from collections import namedtuple

from CLASSES.arrow import Arrow, ArrowProfile
from constantes import *

class Bow:

    def __init__( self , Power = 100 , MaxPull = MAX_PULL, WetDebuff = WET_DEBUFF ):

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
        Energy = d*( k*( x**2 ) )

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
        self.Theta = numpy.clip( Theta , MIN_THETA , MAX_THETA)

    def setPull( self , Pull : float ):
        self.Pull = numpy.clip( Pull , 0 , MAX_PULL )

