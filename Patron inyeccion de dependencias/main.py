from computadora import *
from mouse import *
from monitor import *
from teclado import *


def main():
    teclado1 = Teclado_genius("Genius", "Inalambrico") 
    mouse1 = Mouse_redDragon("Red Dragon", "Alambrico")
    monitor1 = Monitor_asus("180", "Asus")

    computadora = Computadora(monitor1, teclado1, mouse1)
    computadora.componentes()

if __name__=="__main__":
    main()