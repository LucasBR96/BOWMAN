import numpy
import func_tools

class Arrow:

    def __init__( self, initial_speed, theta, length, s_mass , h_mass, base_pos, L ):

        self.speed = initial_speed
        self.theta = theta
        self.s_mass = s_mass
        self.h_mass = h_mass
        self.base_pos = base_pos
        self.L = L
        self.acc = numpy.zeros( 2 )

    def get_grav_center( self ):

        return ( ( self.L/2)*self.s_mass + self.L*self.h_mass )/( self.s_mass + self.h_mass )


        
