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
párnym ID, ktorí v našom prípade predstavuje praváka sa pokúsi najprv vziať pravú vidličku. Na riadku 57 je tento proces 
reprezentovaný funkciou **wait()**, ktorá dekrementuje hodnotu semafora, ak je hodnota 0, tak vlákno čaká. Potom sa filozof 
pokúsi vziať ľavú vidličku ak je voľná ak nie, tak musí čakať, pretože potrebuje dve vidličky k tomu aby sa najedol. Potom 
keď má filozof obidve vidličky môže sa navečeriať. Ak doje vráti vidličky naspäť na svoje miesto, to znamená, že v kóde 
na riadku 69 a 71 sa inkremetuje semafor naspäť na hodnotu jedna.

## Odôvodnenie

Riešenie problému pomocou pravákov a ľavákov zabráňuje uviaznutiu v programe. Filozofi na párnom indexe sa snažia najprv 
vziať pravú vidličku a ľavú si nevšímajú dokedy najprv nemajú v ruke pravú. Filozofi na nepárnom indexe zase postupujú naopak. 
To znamená že ak pri sebe sedia pravák a ľavák, tak ak ľavák vezme skôr svoju ľavú vidličku, tak pravák už má svoju obsadenú a musí čakať 
dokedy nedoje ľavák. Vďaka tomu že pravák musí čakať na svoju pravú vidličku tak neberie do rúk zbytočne ľavú, čím nenastáva deadlock. 
V tom najlepšom prípade jedia naraz dvaja filozofi a v najhoršom jeden. Vyhladovanie v tomto prípade nenastane, pretože 
filozof ktorí má jednu vidličku v ruke si ako keby rezervuje miesto a čaká už len kedy doje filozof vedľa neho. Takýmto spôsobom 
sa nakoniec navečeria každý a nenastane, že nejaký filozof vyhladovie.

Ďalším riešením je aj riešenie pomocou tokenu. Spočíva v tom, že k vidličkám môže pristupovať iba ten kto má token, keď doje tak posunie 
token inému filozofovi. Tým sa zabráni deadlocku, preotže v jednom čase môže jesť iba jeden filozof na rozdiel riešenia s ľavákmi 
a pravákmi, kde môžu v jednom čase jesť aj dvaja. Naopak riešenie s tokenom lepšie oraganizuje prideľovanie jedla a tak sa 
každý filozof naje rovnako.

Riešenie s časníkom, spočíva v tom, že časník sa umožní najesť iba N-1 filozofom a jeden čaká pred bariérou. V tomto riešení 
sa takto eliminuje deadlock, pretože ak by aj každý vzal jednu vidličku, vždy ostane jedna voľná a tak sa môže najesť aspoň 
jeden filozof. Následne ak filozof doje môže sa pokúsiť navečeriať filozof, ktorí čakal pred bariérou. 

Z pohľadu vyhladovania je najlepším riešením riešenie s tokenom, pretože vieme zabezpečiť prísun jedla v konštantnom čase 
každému filozofovi. Zase z pohľadu efektívnosti nie je dané riešenie najlepšie, pretože v jednom čase vie jesť iba jeden filozof. 
Lepšími riešeniami sú riešenia pomocou ľavákov a pravákov alebo pomocou časníka, kde v jednom čase vedia jesť prípadne aj dvaja filozofi, 
nevýhodou je, že niektorí filozofi sa najedia viackrát za daný čas iný menej. 

