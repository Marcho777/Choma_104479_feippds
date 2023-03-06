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

