"""
"""

__authors__ = "Marián Choma"
__email__ = "xchoma@stuba.sk"
__license__ = "MIT"

from fei.ppds import Mutex, Thread, Semaphore, print
from time import sleep
from random import uniform

POC_FILOZOFOV = 5
POC_KOL = 10


class Zdielane:
    """Represent shared data for all threads."""
    def __init__(self):
        """Initialize an instance of Shared."""
        self.vydlicky = [Semaphore(1) for _ in range(POC_FILOZOFOV)]


def rozmyslanie(i):
    print(f"Filozof {i} rozmýšľa")
    sleep(0.1)


def veceranie(i):
    print(f"Filozof {i} večeria")
    sleep(0.2)


def filozof(i: int, zdielane: Zdielane):
    """Run philosopher's code.
    Args:
        i -- philosopher's id
        shared -- shared data
    """
    for _ in range(POC_KOL):
        rozmyslanie(i)
        # get forks
        left_fork = i
        right_fork = (i + 1) % POC_FILOZOFOV
        if i % 2 == 0:
            zdielane.vydlicky[left_fork].wait()
            print(f"Filozof {i} si vzal lavu vydlicku a caka na pravu")
            zdielane.vydlicky[right_fork].wait()
            print(f"Filozof {i} si vzal pravu vydlicku a moze jest")
        else:
            zdielane.vydlicky[right_fork].wait()
            print(f"Filozof {i} si vzal pravu vydlicku a caka na pravu")
            zdielane.vydlicky[left_fork].wait()
            print(f"Filozof {i} si vzal lavu vydlicku a moze jest")
        veceranie(i)
        # put forks back
        zdielane.vydlicky[left_fork].signal()
        print(f"Filozof {i} vratil lavu vidlicku")
        zdielane.vydlicky[right_fork].signal()
        print(f"Filozof {i} vratil pravu vidlicku")

def main():
    """Run main."""
    zdielane: Zdielane = Zdielane()
    filozofi: list[Thread] = [
        Thread(filozof, i, zdielane) for i in range(POC_FILOZOFOV)
    ]
    for p in filozofi:
        p.join()


if __name__ == "__main__":
    main()
