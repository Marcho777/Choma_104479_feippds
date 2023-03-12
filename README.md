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