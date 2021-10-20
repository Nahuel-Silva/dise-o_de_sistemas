from abc import *

class Isueldo():

    @abstractmethod
    def __init__(self, sueldo):
        pass
    
    @abstractstaticmethod
    def get_sueldo(self):
        pass