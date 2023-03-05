"""
"""

__authors__ = "Marián Choma, Marián Šebeňa"
__email__ = "xchoma@stuba.sk, mariansebena@stuba.sk, xvavro@stuba.sk"
__license__ = "MIT"

from fei.ppds import Mutex, Thread, Semaphore, print
from time import sleep
from random import uniform

C = 5
N = 3


class Shared(object):

    def __init__(self):
        self.mutex = Mutex()
        self.cakaren = 0
        self.zakaznik = Semaphore(0)
        self.holic = Semaphore(0)
        self.zakaznik_ostrihany = Semaphore(0)
        self.holic_dostrihal = Semaphore(0)


def get_haircut(i):
    sleep(0.5)
    print(f"Zákaznik {i} sa strihá.")


def cut_hair():
    sleep(0.5)
    print("Holič strihá vlasy")


def balk(i):
    print(f"Čakáren je plná. Zakaznik  {i} čaká")
    sleep(uniform(0.5, 1))


def growing_hair(i):
    print(f"Zákazník {i} odišiel a necháva si narásť vlasy")
    sleep(uniform(0.8, 2))


def customer(i, shared):
    while True:
        shared.mutex.lock()
        if shared.cakaren == N:
            shared.mutex.unlock()
            balk(i)

        else:
            shared.cakaren += 1
            print(f'Zákaznik {i} vstúpil do čakárne. Počet ľudí: {shared.cakaren}')
            shared.mutex.unlock()

            shared.zakaznik.signal()
            shared.holic.wait()
            get_haircut(i)
            shared.zakaznik_ostrihany.signal()
            shared.holic_dostrihal.wait()

            shared.mutex.lock()
            shared.cakaren -= 1
            shared.mutex.unlock()
            growing_hair(i)


def barber(shared):
    while True:
        shared.zakaznik.wait()
        shared.holic.signal()
        cut_hair()
        shared.holic_dostrihal.signal()
        shared.zakaznik_ostrihany.wait()


def main():
    shared = Shared()
    customers = []
    for i in range(C):
        customers.append(Thread(customer, i, shared))
    hair_stylist = Thread(barber, shared)

    for t in customers + [hair_stylist]:
        t.join()


if __name__ == "__main__":
    main()
