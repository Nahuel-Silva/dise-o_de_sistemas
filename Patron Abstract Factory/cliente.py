#Cliente
from fordFabrica import *
from toyotaFabrica import *

class Cliente():
    def accion_cliente(self, fabrica):
        coche = fabrica.crear_coche()
        motor = fabrica.crear_motor()
        chasis = fabrica.crear_chasis()

        print(coche.funcion_coche())
        print(chasis.funcion_chasis())
        print(motor.funcion_motor())
