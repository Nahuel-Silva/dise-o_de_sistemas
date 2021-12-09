from banco import *
from ejecutivoCuenta import *
from liderTeamEjecutivo import *
from gerente import *
from director import *

if __name__=="__main__":

    ejecutivoCuenta = EjecutivoCuenta()
    liderTeamEjecutivo = LiderEjecutivo()
    gerente = Gerente()
    director = Director()

    ejecutivoCuenta.set_next(liderTeamEjecutivo)
    liderTeamEjecutivo.set_next(gerente)
    gerente.set_next(director)

    monto = 10000000

    liderTeamEjecutivo.solicitudPrestamo(monto)

    #Si utilizo banco utilizo lo de abajo

    # banco = Banco()

    # monto = 150000

    # banco.ejecutivoCuenta.solicitudPrestamo(monto)


