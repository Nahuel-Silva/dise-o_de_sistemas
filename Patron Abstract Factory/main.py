#Main
from cliente import *

def main():
    c = Cliente()
    print("Fabrica Ford: ")
    c.accion_cliente(FordFabrica())
    print("\nFabrica Toyota: ")
    c.accion_cliente(ToyotaFabrica())

if __name__=="__main__":
    main()