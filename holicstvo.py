"""Tento modul implementuje chod holičstva s predbiehaním.

Problém holičstva s predbiehaním patrí medzi problémy medziprocesovej komunikácie a ilustruje ako sa synchronizujú
vlákna.
"""

__authors__ = "Marián Choma, Marián Šebeňa"
__email__ = "xchoma@stuba.sk, mariansebena@stuba.sk, xvavro@stuba.sk"
__license__ = "MIT"

from fei.ppds import Mutex, Thread, Semaphore, print
from time import sleep
from random import uniform

C = 5  # počet vlákien(zákazníkov)
N = 3  # počet miest v čakárni


class Zdielane(object):
    """Trieda reprezentujúca zdieľané premenné"""
    def __init__(self):
        """Konštruktor inicializuje 4 semafory, vytvorí objekt triedy Mutex a počítadlo pre čakáreň.
        """
        self.mutex = Mutex()
        self.cakaren = 0
        self.zakaznik = Semaphore(0)
        self.holic = Semaphore(0)
        self.zakaznik_ostrihany = Semaphore(0)
        self.holic_dostrihal = Semaphore(0)


def ostrihanie_sa(i):
    """Funkcia pre simuláciu strihania vlasov u zákazníka

    :param i: Id vlákna
    :return:
    """
    sleep(0.5)
    print(f"Zákaznik {i} sa strihá.")


def strihanie_vlasov():
    """Funkcia pre simuláciu strihania vlasov holičom

    :return:
    """
    sleep(0.5)
    print("Holič strihá vlasy")


def cakanie(i):
    """Uspanie vlákna simulujúce čakanie zákazníka ak je čakáreň plná

    :param i: Id vlákna
    :return:
    """
    print(f"Čakáren je plná. Zakaznik  {i} čaká")
    sleep(uniform(0.5, 1))


def rast_vlasov(i):
    """Informuje o dostrihaní zákazníka a simuluje čas na opätovné navštívenie holiča

    :param i: Id vlákna
    :return:
    """
    print(f"Zákazník {i} odišiel a necháva si narásť vlasy")
    sleep(uniform(0.8, 2))


def zakaznik(i, zdielane):
    """Reprezentuje chovanie zákazníka a proces strihania vlasov z pohľadu zákazníka.

    :param i: Id vlákna
    :param zdielane: Objekt triedy Zdielane
    :return:
    """
    while True:
        zdielane.mutex.lock()
        if zdielane.cakaren == N:
            zdielane.mutex.unlock()
            cakanie(i)

        else:
            zdielane.cakaren += 1
            print(f'Zákaznik {i} vstúpil do čakárne. Počet ľudí: {zdielane.cakaren}')
            zdielane.mutex.unlock()

            zdielane.zakaznik.signal()
            zdielane.holic.wait()
            ostrihanie_sa(i)
            zdielane.zakaznik_ostrihany.signal()
            zdielane.holic_dostrihal.wait()

            zdielane.mutex.lock()
            zdielane.cakaren -= 1
            zdielane.mutex.unlock()
            rast_vlasov(i)


def holic(zdielane):
    """Reprezentuje chovanie holiča a proces strihania vlasov z pohľadu holiča.

    :param zdielane: Objekt triedy Zdielane
    :return:
    """
    while True:
        zdielane.zakaznik.wait()
        zdielane.holic.signal()
        strihanie_vlasov()
        zdielane.holic_dostrihal.signal()
        zdielane.zakaznik_ostrihany.wait()


def main():
    """Vytvorenie vlákien a objektu triedy Zdielane.

    :return:
    """
    shared = Zdielane()
    customers = []
    for i in range(C):
        customers.append(Thread(zakaznik, i, shared))
    hair_stylist = Thread(holic, shared)

    for t in customers + [hair_stylist]:
        t.join()


if __name__ == "__main__":
    main()
