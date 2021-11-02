from mutant import *
from probar_random import *

def main():
    dna = [ ["A","T","G","C","G","A"],
            ["C","A","G","T","G","C"],
            ["T","T","A","T","G","T"],
            ["A","G","A","A","G","G"],
            ["C","C","C","C","T","A"],
            ["T","C","A","C","T","G"] ]
    # a = random_dna()
    # print("\n",a)
    # mutant(a)
    mutant(dna)


if __name__ == '__main__':
    main()