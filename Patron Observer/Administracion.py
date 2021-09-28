from ILibroMalEstado import *

class Administracion(ILibroMalEstado):
    def update(self, libro):
        if libro.estado.upper() == "MALO":
            print("\nAdministracion: ")
            print(f"Envió una queja formal por el {libro.titulo} debido a devolución en mal estado.")
        else:
            print("\nAdministracion: ")
            print(f"Devolución de {libro.titulo} en buen estado.")