""" Tento modul implementuje problém hodujúcich divochov.
Implemetácia využíva riešenie s jedným kuchárom.
"""

__authors__ = "Marián Choma, Tomáš Vavro"
__email__ = "xchoma@stuba.sk, xvavro@stuba.sk"
__license__ = "MIT"

from fei.ppds import Mutex, Thread, Semaphore, print
from time import sleep

POCET_DIVOCHOV: int = 5
KAPACITA_HRNCA: int = 3


class Zdielane:
    """Trieda reprezentuje zdieľané dáta pre všetky vlákna"""

    def __init__(self):
        self.mutex1 = Mutex()
        self.mutex2 = Mutex()
        self.plnyHrniec = Semaphore(0)
        self.prazdnyHrniec = Semaphore(0)
        self.bariera1 = Semaphore(0)
        self.bariera2 = Semaphore(0)
        self.pocitadloBariera = 0
        self.porcie = 0


def kuchar(zdielane: Zdielane):
    """Funkcia simuluje správanie sa kuchára.

    :param zdielane: objekt triedy Zdielane
    :return:
    """
    while True:
        zdielane.prazdnyHrniec.wait()

        zdielane.porcie = KAPACITA_HRNCA
        sleep(0.5)

        print("Kuchar: navaril som jedlo a dal som ho do hrnca")
        zdielane.plnyHrniec.signal()


def divoch(id: int, zdielane: Zdielane):
    """Funkcia reprezentuje správanie sa divocha.

    :param id: id vlákna divocha
    :param zdielane: objekt triedy Zdielane
    :return:
    """
    while True:
        zdielane.mutex1.lock()
        zdielane.pocitadloBariera += 1
        print(f"Divoch {id}: prišiel som na večeru je nás {zdielane.pocitadloBariera}")
        sleep(0.5)
        if zdielane.pocitadloBariera == POCET_DIVOCHOV:
            print(f"Divoch {id}: už sme všetci, môžme začať večerať.")
            zdielane.bariera1.signal(POCET_DIVOCHOV)
        zdielane.mutex1.unlock()
        zdielane.bariera1.wait()

        zdielane.mutex1.lock()
        zdielane.pocitadloBariera -= 1
        if zdielane.pocitadloBariera == 0:
            zdielane.bariera2.signal(POCET_DIVOCHOV)
        zdielane.mutex1.unlock()
        zdielane.bariera2.wait()

        zdielane.mutex2.lock()
        print(f"Divoch {id}: počet porcií v hrnci {zdielane.porcie}")
        if zdielane.porcie == 0:
            print(f"Divoch {id}: budím kuchára, prázdny hrniec")
            zdielane.prazdnyHrniec.signal()
            zdielane.plnyHrniec.wait()
        zdielane.porcie -= 1
        print(f"Divoch {id}: beriem si porciu. Pocet porcii v hrnci: {zdielane.porcie}")
        sleep(0.5)
        zdielane.mutex2.unlock()

        print(f"Divoch {id}: hodujem")
        sleep(0.5)


def main():
    """Vytvorenie vlákien a objektu triedy Zdielane.
    :return:
    """
    zdielane: Zdielane = Zdielane()
    divosi: list[Thread] = [Thread(divoch, i, zdielane) for i in range(POCET_DIVOCHOV)]
    kucharPole = Thread(kuchar, zdielane)
    for p in divosi + [kucharPole]:
        p.join()


if __name__ == "__main__":
    main()
