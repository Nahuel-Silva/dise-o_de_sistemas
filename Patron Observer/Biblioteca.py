from Administracion import *
from Compras import *
from Stock import *
from AlarmaLibro import *

class Biblioteca:
    
    @staticmethod
    def devuelve_libro(libro):
        print(f"\n------>Informe devolución de {libro.titulo}<------")
        attach_array = [Administracion(), Compras(), Stock()]
        AlarmaLibro.multi_attach(attach_array)
        AlarmaLibro.notify_observers(libro)