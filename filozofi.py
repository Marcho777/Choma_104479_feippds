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
        left_fork = i
        right_fork = (i + 1) % POC_FILOZOFOV
        if i % 2 == 0:
            zdielane.vidlicky[right_fork].wait()
            print(f"Filozof {i} si vzal pravu vydlicku a caka na lavu.")
            zdielane.vidlicky[left_fork].wait()
            print(f"Filozof {i} si vzal lavu vydlicku a zacal jest")
        else:
            zdielane.vidlicky[left_fork].wait()
            print(f"Filozof {i} si vzal lavu vydlicku a caka na pravu")
            zdielane.vidlicky[right_fork].wait()
            print(f"Filozof {i} si vzal pravu vydlicku a moze zacat jest")

        veceranie(i)

        zdielane.vidlicky[left_fork].signal()
        print(f"Filozof {i} vratil lavu vidlicku")
        zdielane.vidlicky[right_fork].signal()
        print(f"Filozof {i} vratil pravu vidlicku")


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
