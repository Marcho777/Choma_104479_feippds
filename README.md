# Večerujúci filozofi

## Popis

Úlohou tohto zadania je implemetácia problému večerujúcich filozofov, pomocou zavedenia riešenia ľavákov a pravákov. 
Problém spočíva v tom, že pri jednom stole sedia piati filozofi, ktorí rozmýšaljú. Na stole je päť vidličiek, iba jedna
vidlička je medzi dvoma filozofmi. Ak sa chce filozof najesť musí vziať obe vidličky, ktoré ma pri sebe. Potom ak dovečeria,
tak vidličky vráti naspäť na svoje miesto. Správne riešenie by malo spočívať v tom, že nenastane *deadlock* a žiaden filozof 
nevyhladuje, to znamená, že sa na dlhú dobu nedostane k mise.

## Inštalácia

Program je implementovaný v jazyku Python 3.10. Využíva modul **fei.ppds**, ktorý sa dá doinštalovať
v operačnom systéme Windows pomocou príkazu ```py -3 -m pip install --upgrade fei.ppds```.

## Vysvetlenie

Program má triedu **Zdielane** ´, ktorá je definovaná na 17 riadku. Daná trieda slúži na inicializáciu vidličiek. Parameter 
**vidlicky** je pole veľkosti premennej **POC_FILOZOFOV** definovanej na riadku 13. V danom poli sú semafory nastavené na 
hodnotu 1, to znamená, že vidličky nie sú obsadené. 

Funkcia **rozmyslanie** definovaná na 26 riadku, simuluje čas potrebný na rozmýšľanie filozofa. Podobne aj funkcia
**veceranie** definovaná na 35 riadku, ktorá simuluje čas potrebný na večerania u nejakého filozofa.

Správanie sa filozofa je implementované vo funkcii **filozof** na 45 riadku. Vo for cykle najprv filozof rozmýšľa a potom 
sa mu priradí ľavá a pravá vidlička podľa jeho ID. Napríklad ak je to filozof 3, tak vidličky, ktoré má pri sebe budú 
na indexe 3 a 4. V tomto riešení na párnych miestach sedia praváci a na nepárnych zase ľaváci. To znamená, že proces s 
párnym ID, ktorí v našom prípade predstavuje praváka sa pokúsi najprv vziať pravú vidličku. Na riadku 57 