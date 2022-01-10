import numpy
import functools
from collections import namedtuple

from arrow import Arrow, ArrowProfile
from bow import Bow
from constantes import *

class Bowman:

    def __init__( self , Inventory, Bow, Position = DEFAULT_X ):

        self.HP = MAX_HEALTH
        self.Stamina = MAX_STAMINA

        self.Bow = Bow
        self.Inventory