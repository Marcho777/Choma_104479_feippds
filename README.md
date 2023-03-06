# Holičstvo s predbiehaním

## Popis

Úlohou tohto zadania je implementácia synchronizačného problému holičstva s predbiehaním. Holičstvo pozostába z dvoch 
miestností: 
* Čakáreň pre N klientov
* Miestnosť holiča

Ak nie je žiadny klient, tak holič spí. Klient ak bude chcieť vojsť do holičstva: 
* A všetky stoličky v čakárni sú obsadené, tak odíde
* A holič je obsadený, ale je voľná stolička, sadne si a čaká
* A holič spí, zobudí ho, sadne si a čaká

## Inštalácia

Program je implementovaný v jazyku Python 3.10. Využíva modul **fei.ppds**, ktorý sa dá doinštalovať
v operačnom systéme Windows pomocou príkazu ```py -3 -m pip install --upgrade fei.ppds```.

## Vysvetlenie

Program má triedu *Zdielane*, ktorá je definovaná na riadku 19. Daná trieda slúži na inicializáciu počtu zákazníkov v čakárni, 
mutexu a štyroch semaforov z modulu **fei.ppds**, ktoré majú počiatočnú hodnotu nula. Na riadku 71 je definovaná funkcia 
**zákazník**, ktorá simuluje správanie zákazníka v holičstvu a na riadku 101 je implementovaná fukcia **holic**, ktorá 
reprezentuje chovanie holiča. 


V nekonečnom cykle vo funkcii **zakaznik** najprv uzamkneme **mutex** aby do kritickej časti kódu mohol vstúpiť iba jeden proces.
Tu skontrolujeme koľko ľudí je v čakárni, ak je čakáreň plná odomkneme **mutex** a uspíme vlákno pomocou funkcie **cakanie** definovanou 
na riadku 51. V prípade, že je v čakárni voľné miesto zvýšime počet ľudí v čakárni a urobíme signál semafora **zakaznik** z objektu 
**zdielane**, ktorý na zvýši jeho hodnotu na 1. Následne sa proces zastaví pomocou funkcie **wait** semafora **holic** na 90 riadku, pretože je jeho hodnota 0. 

Vo funkcii **holic** proces čakal na 108 riadku na signal z semafora **zakaznik**, kde ho pomocou funkcie **wait()** nastaví naspäť na 0. Tento proces 
simuluje to, že zákazník zobudí holiča. Ten mu potom, pošle signál naspäť pomocou semafora **holic** na 109 riadku. To znamená 

