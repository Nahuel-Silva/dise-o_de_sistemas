from isubject import *

class CanalYoutube(Isubject):
    
    def __init__(self):
        self.subscriptores = []
        self.ultimoVideo = ""

    def attach(self, observer):
        self.subscriptores.append(observer)
    
    def detach(self, observer: Observer):
        for subscriptor in self.subscriptores:
            if subscriptor == observer:
                self.subscriptores.pop(subscriptor)

    def notify(self):
        for subscriptor in self.subscriptores:
            subscriptor.update()

    def agregaVideo(self, titulo):
        self.ultimoVideo=titulo
        self.notify()
        print("Nuevo video agregado al canal")

    def get_ultimoVideo(self):
        return self.ultimoVideo