from CLASSES.arrow import Arrow

class camera:

    def __init__( self ):

        self.focus = None
    
    def focus_at( self , obj ):
        self.focus = obj
    
    def get_focus( self ):

        focus = self.focus
        if isinstance( focus , Arrow ):
            return focus.Center