class Monitor():
    def __init__(self, pulgadas, marca):
        self._pulgadas = pulgadas
        self._marca = marca

    def monitor(self):
        pass

class Monitor_asus(Monitor):
    def __init__(self, pulgadas, marca):
        super().__init__(pulgadas, marca)

    def monitor(self):
        print(f"Soy el monitor {self._marca}")

class Monitor_LG(Monitor):
    def __init__(self, pulgadas, marca):
        super().__init__(pulgadas, marca)
    
    def monitor(self):
        print(f"Soy el monitor {self._marca}")

class Monitor_aorus(Monitor):
    def __init__(self, pulgadas, marca):
        super().__init__(pulgadas, marca)
    
    def monitor(self):
        print(f"Soy el monitor {self._marca}")