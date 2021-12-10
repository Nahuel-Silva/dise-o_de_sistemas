from observer import *
from isubject import *

class Subscriptor(Observer):

    def __init__(self, subject: Isubject):
        self.subject = subject

    def update(self):
        print("Video publicado!!!\nA mirarlo!!!")
        print(f"Video: {self.subject.get_ultimoVideo()}")