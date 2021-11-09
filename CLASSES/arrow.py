import numpy
import functools

class Arrow:

    '''
    Essa flecha é considerada "simples" no sentido que é fisicamente tratada como um ponto
    material. Suas coordenadas são dadas pelo centro da flecha; o cabo é sempre alinhado com a direção 
    do movimento, etc. Não há efeito de alavanca causado pelo vento ou distribuição de massa da flecha.
    Isso torna a balística menos realista, porém melhor computável
    '''

    def __init__( self , mass , center , L , speed ):

        self.mass = mass
        self.speed = speed # numpy.ndarray com 2 dimensões
        self.L = L # comprimento da flecha
        self.center = center

        self.flying = True
        self.acc    = numpy.zeros( 2 )

    def get_angle( self ):

        vx = self.speed[ 0 ]
        vy = self.speed[ 1 ]

        return numpy.arctan( vy/vx )
    
    def move( self , dt , **kwargs ):

        self.acc = self.update_acc( kwargs )
        self.speed = self.speed + self.acc*dt
        self.center = self.center + self.speed*dt

    def update_acc( self , **kwargs ):

class complexArrow:

    def __init__( self, initial_speed, theta, length, s_mass , h_mass, base_pos, L ):

        self.speed = initial_speed
        self.theta = theta
        self.s_mass = s_mass
        self.h_mass = h_mass
        self.base_pos = base_pos
        self.L = L
        self.acc = numpy.zeros( 2 )
    
    @functools.lru_cache()
    def get_grav_center( self ):

        return ( ( self.L/2)*self.s_mass + self.L*self.h_mass )/( self.s_mass + self.h_mass )


        
