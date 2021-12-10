from abc import *
from observer import * 

class Isubject(metaclass=ABCMeta):

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass

    