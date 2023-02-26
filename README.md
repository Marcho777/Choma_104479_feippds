# Bakery algoritmus

## Popis

Úlohou tohto zadania je implementácia bakery algoritmu v jazyku python a taktiež odôvodnenie, prečo je bakery
algoritmus korektné riešenie problému vzájomného vylúčenia.

## Inštalácia

Algoritmus je implementovaný v jazyku Python 3.10. Program taktiež využíva modul **fei.ppds**, ktorý sa dá doinštalovať
v operačnom systéme Windows pomocou príkazu ```py -3 -m pip install --upgrade fei.ppds```.

## Vysvetlenie 

Bakery algoritmus využíva 2 polia. Prvé pole reprezentuje poradie v akom vstupujú vlákna do algoritmu a druhé pole slúži 
na označenie, že sa dokončilo priradenie a inkrementácia maximálneho čísa z poľa poradie. Druhé pole je potrebné, pretože
inkrementácia a vybranie maximálneho čísla z poľa nie je atomická operácia.

## Príklad

Máme 3 vlákna V1,V2,V3. Vytvoríme si pole s názvom poradie ktoré bude obsahovať iba 0 [0,0,0] a pole vybrany, ktoré bude
obsahovať [False, False, False]. Do algoritmu môže vstúpiť napríklad V1 s ID 0, takže sa vybrany[0] prepíše na True, to 
taktiež urobí aj V3 takže pole vybrany bude vyzerat takto [True, False, True]. Môže sa stať, že V1 a V3 urobia naraz 
inkrementáciu maximalného čísla z poľa poradie. To bude znamenať, že pole poradie bued vyzerať takto [1,0,1]. V3 môže
napríklad ďalej pokračovať v kóde, to znamená, že v poli vybrany sa nastavý hodnota naspäť na False, vojde do for cyklu a 
uviazne vo while cykle, pretože pole vybrany[0] je True. V2 prejde kódom do for cyklu, pole vybrany bude [True, False, False], 
takže obidve vlákna čakajú na pole V1. Ak prepínač naspäť prepne na vlákno V1 tak sa všade v poli vybrany bude False.

