from abc import ABCMeta, abstractmethod

class IAprobador(metaclass=ABCMeta):
            
    @abstractmethod
    def set_next(self):
        pass

    @abstractmethod
    def solicitudPrestamo(self, monto):
        pass