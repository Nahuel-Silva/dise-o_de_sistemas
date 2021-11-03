class Computadora():
    def __init__(self, monitor, teclado, mouse):
        self._monitor = monitor
        self._teclado = teclado
        self._mouse = mouse

    def componentes(self):
        print("\nMis componentes son:\n")
        self._monitor.monitor()
        self._teclado.teclado()
        self._mouse.mouse()