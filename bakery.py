""" Tento modul implementuje Bakery algoritmus

Bakery algoritmus zabezpečuje vzájomné vylúčenie N vlákien tak, aby sa zabránilo
viacerým vstupom do kritických častí kódu.
"""

__author__ = "Marián Choma"
__email__ = "xchoma@stuba.sk"
__license__ = "MIT"

from fei.ppds import Thread
from time import sleep

pocetVlakien: int = 10  # premnenná na zadefinovanie počtu vlákien
index: int = 0
poradie: list[int] = [0] * pocetVlakien
vybrany: list[bool] = [False] * pocetVlakien


def vstup(i: int):
    """Reprezentuje vstup do bakery algoritmu pred kritickou sekciou.

    Arguments:
        i      -- Id vlákna
    """
    vybrany[i] = True
    poradie[i] = 1 + max(poradie)
    vybrany[i] = False
    for j in range(pocetVlakien):
        while vybrany[j]:
            continue
        while poradie[j] != 0 and (poradie[j] < poradie[i] or (poradie[j] == poradie[i] and j < i)):
            # hľadanie najmenšieho poradového čísla s najmenším indexom v poradovom poli inak proces čaká
            continue


def vystup(i: int):
    """Výstup z bakery algoritmu po ktitickej sekcii.

    Arguments:
        i      -- Id vlákna
    """
    poradie[i] = 0


def bakery(s, i):
    """Simulácia procesu bakery algoritmu.

    Kritická sekcia predstavuje inkremetovanie globálnej premennej index.
    Pre demonštráciu je použitá funkcia print pre výpis do konzoly premennej index a reťazca popisujúceho vlákno.

    Arguments:
        i -- Id vlákna
        s -- reťazec reprezentujúci poradie vlákna
    """
    global index
    vstup(i)
    index += 1
    print(s, index)
    vystup(i)


if __name__ == '__main__':
    threads = [Thread(bakery, f"vlakno {i + 1} ", i) for i in range(pocetVlakien)]  # i+1 pretože Id vlákna začína od 1
    [t.join() for t in threads]
