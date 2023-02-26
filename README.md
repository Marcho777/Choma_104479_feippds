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
inkrementáciu maximalného čísla z poľa poradie. To bude znamenať, že pole poradie bude [1,0,1]. Prepínač prepne na vlákno 
V3, ktoré bude ďalej pokračovať v kóde, to znamená, že v poli vybrany sa nastavý hodnota naspäť na False, vojde do 
for cyklu a uviazne vo while cykle, pretože pole vybrany[0] je True. V2 prejde kódom do for cyklu, pole vybrany bude 
[True, False, False], takže obidve vlákna čakajú na pole V1. Ak prepínač naspäť prepne na vlákno V1 tak pole vybrany bude 
všade len False. Vlákna V2 a V3 uviaznú v druhom while, pretože V1 má menšie poradové číslo ako V2. V3 má síce rovnaké 
poradové číslo ako V1, ale v poli sa nachádza V1 skôr a tak musí vlákno V3 čakať. Do kritickej časti vstúpi prve vlákno 
V1 a jeho poradové číslo sa nastaví na 0, potom sa vykoná vlákno V3, pretože má najmenšie číslo a nakoniec vstúpi do
kritickej sekcie vlákno V2. Vďaka Bakery algortimu sme docielili, že do kritickej sekcie mohlo vstúpiť iba jedno vlákno.

## Odôvodnenie

Bakery algoritmus je korektné riešenie problému vzájomného vylúčenia, pretože spĺňa 4 podmienky korektného riešenia. 
1. Prvá podmienka hovorí o tom, že v kritickej časti sa smie vykonávať najviac jeden proces, to je splnené, pretože vždy sa v 
kritickej časti vykoná proces s najmenším poradovým číslom a je v poradovom poli na menšom indexe ako ostatné procesy s 
rovnakým poradovým číslom.
2. Žiaden proces, ktorý sa vykonáva mimo kritickej oblasti nesmie brániť iným vstúpiť do nej. Aj táto podmienka je splnená,
pretože procesu, ktorý vstupuje do kritickej oblasti ostatné procesy nijako nebránia vsúpiť do kritickej oblasti s najväčšou 
pravdepodobnosťou sú zaseknuté v nejakom while cykle.
3. Rozhodnutie o vstupe musí príjsť v konečnom čase. Táto podmienka hovorí o tom, že nesmie nastať situácia, že sa zaseknú 
všetky procesy v nejakom prípade a ani jeden nevstúpi do kritickej časti kódu. V Bakery algoritme daná situácia nenastane. 
V prvom while sa zaseknú procesy, len kvôli tomu, že ešte sa nepriradilo všetkým procesom poradové číslo. V druhom while 
sa prechádza poľom a hľadá sa proces, ktorý má najmenšie poradové číslo. Tieto procesy sa musia skončiť v konečnom čase, 
niekedy musí nastať situácia, že prepínač prepne na proces s najmenším poradovím číslom.
4. Procesy nesmú pri vstupe do kritickej oblasti predpokladať nič o vzájomnom časovaní(plánovaní). V Bakery algoritme
procesy pri vstupe do kritickej oblasti nevedia o iných procesoch, ktoré sú na rade. Nemôžeme ani naplánovať, že 
naríklad proces P2 pôjde až po procesu P1 keď vykoná kritickú časť kódu. Proces vstupuje do kritickej oblasti len ak má 
najmenšie poradové číslo a najmenší index s daným číslom, pričom si proces ani nikde neukladá aktuálne najmenšie číslo.  