from CLASSES.bow import Bow
from CLASSES.bowman import Bowman
from UTILS.conv import Conv
from CLASSES.arrow import Arrow
from constantes import *

import numpy as np

class Match:

    def __init__( 
        self, Lenght : float = FIELD_LEN,
        BowmanDist   : float = BOW_MAN_DIST,
        WindSpeed    : float = WIND_SPEED
    ):
        
        self.Lenght = Lenght
        self.BowmanDist = BowmanDist
        self.WindSpeed = WindSpeed

        self.Arrows = []
        self.CurrentArrow = None

    def add_arrow( self , theta , pos ):

        c = np.cos( theta )
        s = np.sin( theta )
        
        a = Arrow( None , pos , ) 


