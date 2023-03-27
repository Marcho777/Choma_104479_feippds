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

Program má na riadku 12 definovanú premenné **POCET_DIVOCHOV** pre zadefinovanie počtu vlákien, ktoré
v tomto prípade predstavujú divochov. Na riadku 13 je zadefinovaná premenná **KAPACITA_HRNCA** Táto premenná 
slúži ako hranica pre kuchára, koľko môže najviac navariť a danú hranicu nesmie v priebehu programu prekročiť. 
Na riadku 16 je trieda **Zdielane**, v ktorej sme si inicializovali zdieľané dáta pre všetky vlákna. 


![Vypis z konzoly](/kuchar.png)


Funkcia **kuchar** je definovaná na riadku 30. Vnútri funkcie sa nachádza nekonečný while cyklus v ktorom na 37 riadku 
je použitý synchronizačný vzor *Semafor*, ktorý čaká pomocou metódy **wait** na signál od divocha, že je hrniec prázdny. Keď 
dostane signál, tak môže pokračovať ďalej v kóde, kde na 38 riadku je použitý ďalší synchronizačný vzor *Mutex*. Slúži na 
uzamknutie vlákna pretože pristupujeme ku zdieľanej premennej **porcie**, tu nastavíme na 39 riadku počet porcií na maximálnu 
kapacitu hrnca a následne môžeme odomknúť vlákno. Na konci while cyklu signalizujeme pomocou druhého semaforu, že kuchár doplnil 
hrniec, a tak môžu divosi pokračovať v hodovaní.

![Vypis z konzoly](/bariera.png)


Funkcia **divoch** implementovaná na riadku 46 simuluje správanie sa divocha. V nekonečnom while cykle je implementovaná 
znovupoužiteľná bariéra, ktorú môžete vidieť na obrázku. Slúži na to aby sa divosi na začiatku počklali a až potom prichádzali 
po jednom k hrnci. Znovupoužiteľnú bariéru sme museli použiť preto, lebo bariéru použivame v cykle. Ak by sme použili len jednoduchú 
bariéru tak by fungovala dobre len pri prvom zbehnutí cyklu. 

![Vypis z konzoly](/hodovanie.png)

Na riadku 64 použijeme *Mutex* pre pristupovanie k hrncu, aby sme zabezpečili, že v jednom čase bude mať prístup k hrncu 
len jeden človek. Divoch skontroluje koľko je porcií v hrnci. Keď v hrnci sa nenachádzajú už žiadne porcie tak zobudí kuchára 
na riadku 75 pomocou semafora **prazdnyHrniec**. Na 76 riadku potom divoch čaká, keďže semafor **plnyHrniec** je nastavený na 0. 
Ak kuchár dovarí a inkrementuje hodnotu semafora na 1, divoch môže pokračovať ďalej v kóde, kde si už len vezme porciu z hrnca a 
odomkne **mutex2**. Tým môže k hrncu pristúpiť ďalší divoch a celý tento proces sa opakuje. Na riadku 82 je vypísané do konzoly, 
že divoch hoduje. Hodovať môže viac divochov naraz. Ak divosi dojedia tak sa musia počkať pred bariérou, až keď budú všetci môžu začať 
pristupovať k hrncu. 

## Výpis

![Vypis z konzoly](/vypis.png)

Na obrázku môžete vidieť výpis programu. Kapacita hrnca bola nastavená na 3 a počet divochov na 5. 