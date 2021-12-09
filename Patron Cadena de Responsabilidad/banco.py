from ejecutivoCuenta import *
from liderTeamEjecutivo import *
from gerente import *
from director import *

class Banco():

    def __init__(self):
        self._ejecutivoCuenta = EjecutivoCuenta()
        self._liderTeamEjecutivo = LiderEjecutivo()
        self._gerente = Gerente()
        self._director = Director()

        self._ejecutivoCuenta.set_next(self.liderTeamEjecutivo)
        self._liderTeamEjecutivo.set_next(self.gerente)
        self._gerente.set_next(self.director)