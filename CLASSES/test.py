from arrow import Arrow
import matplotlib.pyplot as pptlt
import numpy

def test_arrow( arrow, dt = .01, repeats = 10 , points = 10**3 ):
    
    xs = numpy.zeros( points )
    ys = numpy.zeros( points )

    for i in range( points ):

        for j in range( repeats ):
            arrow.move( dt )

        x , y = arrow.center
        xs[ i ] = x
        ys[ i ] = y

        if y < 0:
            break

    return xs , ys

def loose( mass , speed , **kwargs ):

    A = Arrow( mass , numpy.zeros( 2 ) , 1 , speed )
