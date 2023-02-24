"""
"""

__author__ = "Marián Choma"
__email__ = "xchoma@stuba.sk"
__license__ = "MIT"

from fei.ppds import Thread
from time import sleep

pocetVlakien: int = 10
index = 0
poradie: list[int] = [0] * pocetVlakien
vybrany: list[bool] = [False] * pocetVlakien


def vstup(i: int):
    vybrany[i] = True
    poradie[i] = 1 + max(poradie)
    vybrany[i] = False
    for j in range(pocetVlakien):
        while vybrany[j]:

            continue
        while poradie[j] != 0 and (poradie[j] < poradie[i] or (poradie[j] == poradie[i] and j < i)):

            continue


def vystup(i: int):
    poradie[i] = 0
