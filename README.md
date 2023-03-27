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
