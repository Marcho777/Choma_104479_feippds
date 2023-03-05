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
        self.zakaznik_ostrihany = Semaphore(1)
        self.holic_dostrihal = Semaphore(1)


def get_haircut(i):
    sleep(uniform(0.2, 1))
    print(f"Zákaznik {i} sa strihá.")


def cut_hair():
    sleep(uniform(0.2, 1))
    print("Holič strihá vlasy")


def balk(i):
    print(f"Čakáren je plná. Zakaznik  {i} čaká")
    sleep(uniform(0.5, 1))


def growing_hair(i):
    sleep(uniform(0.8, 2))


def customer(i, shared):
    while True:
        shared.mutex.lock()
        if shared.cakaren == N:
            balk(i)
        else:
            shared.cakaren += 1
            print(f'Zakaznik {i} vstúpil do čakárne. Počet ľudí: {shared.cakaren}')
        shared.mutex.unlock()
        shared.holic_dostrihal.wait()
        shared.zakaznik.signal()
        shared.holic.wait()
        get_haircut(i)
        shared.holic.wait()
        shared.zakaznik.signal()
        shared.mutex.lock()
        shared.cakaren -= 1
        shared.mutex.unlock()
        print(f"Zákazník {i} odchádza")
        shared.zakaznik_ostrihany.signal()
        growing_hair(i)


def barber(shared):
    while True:
        shared.zakaznik_ostrihany.wait()
        shared.zakaznik.wait()
        shared.holic.signal()
        cut_hair()
        shared.holic.signal()
        shared.zakaznik.wait()
        shared.holic_dostrihal.signal()


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
