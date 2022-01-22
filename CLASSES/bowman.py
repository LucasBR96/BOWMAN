import numpy
import functools
from collections import namedtuple

from CLASSES.arrow import Arrow, ArrowProfile
from CLASSES.bow import Bow
from constantes import *

class Bowman:

    # def __init__( self , Inventory, Bow : Bow, Position = DEFAULT_X ):
    def __init__( self , Position = numpy.array( [ VIRTUAL_DEFAULT_X , 0 ] ) ):
        self.HP = MAX_HEALTH
        self.Stamina = MAX_STAMINA

        # self.Bow         = Bow
        # self.Inventory   = Inventory
        # self.loadedArrow = list( Inventory.keys() )[ 0 ]

        self.Position = Position
        self.Bow = Bow()
    
    def Draw( self , Pull , Theta ):

        self.Bow.setTheta( Theta )
        self.Bow.setPull( Pull )
    
    def updateStamina( self , dt ):
        
        x = self.Bow.Pull
        if x != 0:
            return self.getTired( dt )
        return self.getRest( dt )
    
    def getRest( self , dt ):
        self.Stamina = MAX_STAMINA
        return False

    def getTired( self , dt ):

        Bow = self.Bow
        x = Bow.Pull
        k = Bow.Power
        d = Bow.WetDebuff
        Force = x*k*d

        self.Stamina -= Force*dt*STAMINA_DECAY
        self.Stamina  = max( self.Stamina , 0 )
        return self.Stamina == 0 
    
    def Loose( self ) -> Arrow:

        # ArrowType = self.loadedArrow
        Position  = numpy.array([ self.Position[0] , VIRTUAL_BOW_HEIGHT ] )
        newArrow  = self.Bow.Loose(  Position )

        # self.Inventory[ ArrowType ] -= 1
        self.Bow.setPull( 0 )

        return newArrow


