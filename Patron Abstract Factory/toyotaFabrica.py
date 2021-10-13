#ConcreteFactory1

from fabrica import Fabrica
from motorToyota import *
from cocheToyota import *
from chasisToyota import *

class ToyotaFabrica(Fabrica):

    def crear_motor(self):
        return MotorToyota()

    def crear_coche(self):
        return CocheToyota()

    def crear_chasis(self):
        return ChasisToyota()