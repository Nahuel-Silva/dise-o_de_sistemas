class Mouse():
    def __init__(self, marca, tipo):
        self._marca = marca
        self._tipo = tipo
    
    def mouse(self):
        pass

class Mouse_redDragon(Mouse):
    def __init__(self, marca, tipo):
        super().__init__(marca, tipo)
    
    def mouse(self):
        print(f"Soy el mouse {self._marca}")

class Mouse_logitech(Mouse):
    def __init__(self, marca, tipo):
        super().__init__(marca, tipo)
    
    def mouse(self):
        print(f"Soy el mouse {self._marca}")

class Mouse_genius(Mouse):
    def __init__(self, marca, tipo):
        super().__init__(marca, tipo)
    
    def mouse(self):
        print(f"Soy el mouse {self._marca}")