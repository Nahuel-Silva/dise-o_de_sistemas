from ILibroMalEstado import *

class Compras(ILibroMalEstado):

    def update(self, libro):
        if libro.estado.upper() == "MALO":
            print("\nCompras: ")
            print(f"Solicito cotizacion de reparacion o reposicion de {libro.titulo}.")
        else:
            print("\nCompras: ")
            print(f"Se solicita nueva cotización para {libro.titulo}.")