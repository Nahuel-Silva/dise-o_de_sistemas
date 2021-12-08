from abc import ABCMeta, abstractmethod, abstractstaticmethod

class Isueldo(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, sueldo):
        pass

    @abstractmethod
    def get_sueldo(self):
        pass