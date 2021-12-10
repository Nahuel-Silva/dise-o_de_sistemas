from abc import *

class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass