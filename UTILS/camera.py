from CLASSES.arrow import Arrow
from CLASSES.bowman import Bowman
from constantes import *

class camera:

    def __init__( self ):

        self.focus = None
    
    def focus_at( self , obj ):
        self.focus = obj
    
    def get_focus( self ):

        focus = self.focus
        if isinstance( focus , Arrow ):
            return focus.Center
        elif isinstance( focus , Bowman ):
            a = focus.Position[ 0 ]
            b = 4*VIRTUAL_BOWMAN_HEIGHT
            return numpy.array( [ a , b ] )
