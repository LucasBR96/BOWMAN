import numpy
import functools
from collections import namedtuple

from constantes import *

ArrowProfile = namedtuple( "ArrowProfile" , [ "Mass" , "Lenght" ] ) 

BasicArrow = ArrowProfile( Mass = BASE_MASS , Lenght = BASE_LEN )

class Arrow:

    def __init__( self , Center , Speed, Profile = BasicArrow  ):

        self.Profile = Profile 
        self.Speed   = Speed
        self.Center  = Center
        self.Flying  = True

    def Fly( self , dt ):
        
        if not self.Flying: return
        self.Center += self.Speed*dt

        # print( self.Center )
    
    def Accelerate( self , dt , g = 9.81 , k = 0 ):
        
        #sem velocidade do vento por enquanto

        if not self.Flying: return
        dy = -g*dt

        vx = self.Speed[ 0 ]
        dx = ( -k*( vx**2 )*dt )/self.Profile.Mass

        self.Speed += numpy.array([ dx , dy ])

    def GetEdges( self ):
        
        vx , vy = self.Speed
        mod = vx**2 + vy**2
        u = self.Speed/numpy.sqrt( mod )

        L = self.Profile.Lenght/2
        pos1 = self.Center + u*L
        pos2 = self.Center - u*L
        return pos1 , pos2
    
    def Lock( self ):
        
        p1 , p2 = self.GetEdges()
        if min( p1[ 1 ] , p2[ 1 ] ) < 0:
            self.Flying = False