""" Tento modul implementuje problém večerujúcich filozofov.

Implemetácia využíva riešenie pomocou ľavákov a pravákov.
"""

__authors__ = "Marián Choma, Tomáš Vavro"
__email__ = "xchoma@stuba.sk, xvavro@stuba.sk"
__license__ = "MIT"

from fei.ppds import Thread, Semaphore, print
from time import sleep

POC_FILOZOFOV = 5
POC_KOL = 10


class Zdielane:
    """Trieda reprezentuje zdieľané dáta pre všetky vlákna"""

    def __init__(self):
        """Inicializácia parametru vidličky, ktoré reprezentujú semafory"""
        self.vidlicky = [Semaphore(1) for _ in range(POC_FILOZOFOV)]


def rozmyslanie(i: int):
    """Simuluje čas na premýšľanie.

    :param i: Id vlákna
    :return:
    """
    print(f"Filozof {i} rozmýšľa")
    sleep(0.1)


def veceranie(i: int):
    """Simuluje čas na večeranie

    :param i: Id vlákna
    :return:
    """
    print(f"Filozof {i} večeria")
    sleep(0.2)


def filozof(i: int, zdielane: Zdielane):
    """Reprezentuje správanie filozofa

    :param i: Id vlákna
    :param zdielane: objekt triedy zdielane
    :return:
    """
    for _ in range(POC_KOL):
        rozmyslanie(i)
        lava_vidlicka = i
        prava_vidlicka = (i + 1) % POC_FILOZOFOV
        if i % 2 == 0:
            zdielane.vidlicky[prava_vidlicka].wait()
            print(f"Filozof {i} si vzal pravú vydličku a čaká na ľavú.")
            zdielane.vidlicky[lava_vidlicka].wait()
            print(f"Filozof {i} si vzal ľavú vydličku a začal jesť")
        else:
            zdielane.vidlicky[lava_vidlicka].wait()
            print(f"Filozof {i} si vzal ľavú vydličku a čaká na pravú")
            zdielane.vidlicky[prava_vidlicka].wait()
            print(f"Filozof {i} si vzal pravú vydličku a môže začať jesť")

        veceranie(i)

        zdielane.vidlicky[lava_vidlicka].signal()
        print(f"Filozof {i} vrátil ľavú vidličku")
        zdielane.vidlicky[prava_vidlicka].signal()
        print(f"Filozof {i} vrátil pravú vidličku")


def main():
    """Vytvorenie vlákien a objektu triedy Zdielane.

    :return:
    """
    zdielane: Zdielane = Zdielane()
    filozofi: list[Thread] = [Thread(filozof, i, zdielane) for i in range(POC_FILOZOFOV)]
    for p in filozofi:
        p.join()


if __name__ == "__main__":
    main()
