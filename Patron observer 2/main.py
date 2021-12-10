from subjectConcreto import *
from observerConcreto import *


def main():
    canal = CanalYoutube()
    sub1 = Subscriptor(canal)
    sub2 = Subscriptor(canal)

    canal.attach(sub1)
    canal.attach(sub2)

    canal.agregaVideo("Aprendiendo patronen")

if __name__=="__main__":
    main()