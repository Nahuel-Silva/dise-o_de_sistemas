from ILibroMalEstado import *

class Stock(ILibroMalEstado):
    def update(self, libro):
        if libro.estado.upper() == "MALO":
            print("\nStock: ")
            print(f"Se da de baja el {libro.titulo} por su estado.")
        else:
            print("\nStock: ")
            print(f"El {libro.titulo} vuelve a estar en stock.")