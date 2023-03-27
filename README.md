# Problém hodujúcich divochov


## Popis

Úlohou tohto zadania je implementácia problému hodujúcich divochov s jedným kuchárom. Divosi potrebujú
spoľahlivý systém, v ktorom budú oznamovat’ všetky úkony, ktoré so
spoločným hodovaním súvisia.
* Divosi vždy začínajú jesť spolu. Posledný divoch, ktorý príde, všetkým
signalizuje, že sú všetci a môžu začať hodovať.
* Divosi si po jednom berú svoju porciu z hrnca dovtedy, kým nie je
hrniec prázdny.
* Divoch, ktorý zistí, že už je hrniec prázdny upozorní kuchárov, aby
znovu navarili.
* Divosi čakajú, kým kuchár doplní hrniec.
* Kuchár navarí porcie a vloží ic do hrnca.
* Keď je hrniec plný, divosi pokračujú v hodovaní.
* Celý proces sa opakuje v nekonečnom cykle.


## Inštalácia

Program je implementovaný v jazyku Python 3.10. Využíva modul **fei.ppds**, ktorý sa dá doinštalovať
v operačnom systéme Windows pomocou príkazu ```py -3 -m pip install --upgrade fei.ppds```.

## Vysvetlenie

Program má na riadkoch 12 definovanú premenné **POCET_DIVOCHOV** pre zadefinovanie počtu vlákien, ktoré
v tomto prípade predstavujú divochov. Na riadku 13 je zadefinovaná premenná **KAPACITA_HRNCA** Táto premenná 
slúži ako hranica pre kuchára, koľko môže najviac navariť a danú hranicu nesmie v priebehu programu prekročiť. 
Na riadku 16 je trieda **Zdielane**, v ktorej sme si inicializovali zdieľané dáta pre všetky vlákna. 


![Vypis z konzoly](/kuchar.png)
Funkcia **kuchar** je definovaná na riadku 30. Vnútri funkcie sa nachádza nekonečný while cyklus v ktorom na 37 riadku 
je použitý synchronizačný vzor *Semafor*, ktorý čaká pomocou metódy **wait** na signál od divocha, že je hrniec prázdny. Keď 
dostane signál, tak môže pokračovať ďalej v kóde, kde na 38 riadku je použitý ďalší synchronizačný vzor *Mutex*. Slúži na 
uzamknutie vlákna pretože pristupujeme ku zdieľanej premennej **porcie**, tu nastavíme na 39 riadku počet porcií na maximálnu 
kapacitu hrnca a následne môžeme odomknúť vlákno. Na konci while cyklu signalizujeme pomocou druhého semaforu, že kuchár doplnil 
hrniec a tak môžu divosi pokračovať v hodovaní.