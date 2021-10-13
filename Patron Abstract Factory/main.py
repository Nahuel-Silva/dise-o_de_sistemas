#Main
from cliente import *

def main():
    c = Cliente()
    print("Fabrica Toyota: ")
    c.accion_cliente(CocheFordF())
    print("\nFabrica Ford: ")
    c.accion_cliente(CocheToyotaF())

if __name__=="__main__":
    main()