#ConcreteFactory2

from fabrica import Fabrica
from motorFord import *
from cocheFord import *
from chasisFord import *

class CocheFordF(Fabrica):

    def crear_motor(self):
        return MotorFord()

    def crear_coche(self):
        return CocheFord()

    def crear_chasis(self):
        return ChasisFord()