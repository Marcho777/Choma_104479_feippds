# Bakery algoritmus

## Popis

Úlohou tohto zadania je implementácia bakery algoritmu v jazyku Python a taktiež odôvodnenie, prečo je bakery
algoritmus korektné riešenie problému vzájomného vylúčenia.

## Inštalácia

Algoritmus je implementovaný v jazyku Python 3.10. Program taktiež využíva modul **fei.ppds**, ktorý sa dá doinštalovať
v operačnom systéme Windows pomocou príkazu ```py -3 -m pip install --upgrade fei.ppds```.

## Vysvetlenie 

Bakery algoritmus využíva 2 polia. Prvé pole reprezentuje poradie v akom vstupujú vlákna do algoritmu a druhé pole slúži 
na označenie, že sa dokončilo priradenie a inkrementácia maximálneho čísla z poľa poradie. Druhé pole je potrebné, pretože
inkrementácia a vybranie maximálneho čísla z poľa nie je atomická operácia. Algoritmus pozostáva z for cyklu, ktorí slúži 
na prechádzanie v poradovom polí. Vo for cykle sú 2 while cykly, prvý slúži na čakanie aby sa každému procesu pridelilo
poradové číslo a druhý while cyklus hľadá v poradovom poli najmenšie číslo s najmenším indexom, kvôli tomu, že môže nastať 
situácia kedy budú mať procesy rovnaké poradové číslo a tak sa uprednostní proces s menším indexom v poli. Následne môže proces 
vstúpiť do kritickej časti a po jej vykonaní sa nastaví jeho poradové číslo na 0. Tento proces sa opakuje pokiaľ každý proces
nevykoná kritickú časť a nezmení si svoje poradové číslo naspäť na 0.

## Odôvodnenie

Bakery algoritmus je korektné riešenie problému vzájomného vylúčenia, pretože spĺňa 4 podmienky korektného riešenia. 
1. Prvá podmienka hovorí o tom, že v kritickej časti sa smie vykonávať najviac jeden proces a to je splnené, lebo vždy sa v 
kritickej časti vykoná proces s najmenším poradovým číslom a je v poradovom poli na menšom indexe ako ostatné procesy s 
rovnakým poradovým číslom.
2. Žiaden proces, ktorý sa vykonáva mimo kritickej oblasti nesmie brániť iným vstúpiť do nej. Aj táto podmienka je splnená,
pretože procesu, ktorý vstupuje do kritickej oblasti ostatné procesy nijako nebránia vsúpiť do kritickej časti kódu s najväčšou 
pravdepodobnosťou sú zaseknuté v nejakom while cykle.
3. Rozhodnutie o vstupe musí príjsť v konečnom čase. Táto podmienka hovorí o tom, že nesmie nastať situácia, že sa zaseknú 
všetky procesy v nejakom prípade a ani jeden nevstúpi do kritickej časti kódu. V Bakery algoritme daná situácia nenastane. 
V prvom while sa zaseknú procesy, len kvôli tomu, že ešte sa nepriradilo všetkým procesom poradové číslo. V druhom while 
sa prechádza poľom a hľadá sa proces, ktorý má najmenšie poradové číslo. Tieto procesy sa musia skončiť v konečnom čase, 
niekedy musí nastať situácia, že prepínač prepne na proces s najmenším poradovím číslom.
4. Procesy nesmú pri vstupe do kritickej oblasti predpokladať nič o vzájomnom časovaní(plánovaní). V Bakery algoritme
procesy pri vstupe do kritickej oblasti nevedia o iných procesoch, ktoré sú na rade. Nemôžeme ani naplánovať, že 
naríklad proces P2 pôjde až po procesu P1, keď vykoná kritickú časť kódu. Proces vstupuje do kritickej oblasti, len ak má 
najmenšie poradové číslo a najmenší index s daným číslom. Proces si ani nikde neukladá aktuálne najmenšie číslo.  

## License

[MIT](https://choosealicense.com/licenses/mit/)
