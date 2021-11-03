class Teclado():
    def __init__(self, marca, tipo):
        self._marca = marca
        self._tipo = tipo

    def teclado(self):
        pass


class Teclado_redDragon(Teclado):
    def __init__(self, marca, tipo):
        super().__init__(marca, tipo)

    def teclado(self):
        print(f"Soy el teclado {self._marca}")

class Teclado_logitech(Teclado):
    def __init__(self, marca, tipo):
        super().__init__(marca, tipo)

    def teclado(self):
        print(f"Soy el teclado {self._marca}")

class Teclado_genius(Teclado):
    def __init__(self, marca, tipo):
        super().__init__(marca, tipo)

    def teclado(self):
        print(f"Soy el teclado {self._marca}")