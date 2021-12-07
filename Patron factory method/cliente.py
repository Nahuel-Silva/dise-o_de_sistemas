
from factoryMethod import FactoryMethod


def main():
    frabrica = FactoryMethod()
    triangulo = frabrica.creador_de_triangulos(10,10,30)
    triangulo.get_description()
    triangulo.get_superficie()

if __name__=="__main__":
    main()