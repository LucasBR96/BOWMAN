import time

class Clock:

    def __init__( self ):

        self.last_t = time.time()
        self.last_dt = 0
    
    def tick( self ):

        t = time.time()
        self.last_dt = t - self.last_t
        self.last_t = t
