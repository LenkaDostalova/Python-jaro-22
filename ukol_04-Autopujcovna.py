""" Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
4A2 3020	Peugeot 403 Cabrio	47534
1P3 4747	Škoda Octavia	41253
Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

registrační značka automobilu,
značka a typ vozidla,
počet najetých kilometrů,
informaci o tom, jestli je vozidlo aktuálně volné (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).
Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu. Poslední atribut nastav jako True, tj. na začátku je vozidlo volné.

Vytvoř objekty, které reprezentují všechny automobily půjčovny.

Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu, který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto().

Otestuj, že program nedovolí půjčit stejné auto dvakrát. 

Přidej třídě Auto metodu vrat_auto(), která bude mít (krom obligátního self) 2 parametry, a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal. Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return."""

class Auto: 
    def __init__(self, registracni_znacka, znacka_a_typ_vozidla, pocet_najetych_kilometru): 
        self.registracni_znacka = registracni_znacka
        self.znacka_a_typ_vozidla = znacka_a_typ_vozidla
        self.pocet_najetych_kilometru = pocet_najetych_kilometru
        self.volne = True
    def __str__(self): 
        return f'Auto s registracní značkou {self.registracni_znacka} je {self.znacka_a_typ_vozidla}.'
    def pujc_auto(self):
        if self.volne == True:
            self.volne = False
            return 'Potvrzuji zapůjčení vozidla'
        else:
            return 'Vozidlo není k dispozici'
    def vrat_auto(self,stav_tachometru,pocet_dni):
        self.stav_tachometru = stav_tachometru
        self.volne = True
        if pocet_dni <= 7:
            cena = 400*pocet_dni
        else:
            cena = 300*pocet_dni
        return f'Potvrzuji vrácení vozidla {self.znacka_a_typ_vozidla}, stav na tachometru je {self.stav_tachometru}. Cena za vypůjčení auta je {cena} Kč.'

peugeot = Auto ('4A2 3020','Peugeot 403 Cabrio',47534)
#print(peugeot)

skoda = Auto('1P3 4747','Škoda Octavia',41253)
#print(skoda)


def vypujcka():
    typ = input('Přejete si vypůjčit auto Škoda nebo Peugeot?: ')
    if typ == 'Škoda':
        print(skoda.pujc_auto())
    elif typ == 'Peugeot':
        print(peugeot.pujc_auto())
    else:
        print('Tento typ auta v půjčovně nemáme.')

def vraceni():
    typ = input('Přejete si vrátit auto Škoda nebo Peugeot?: ')
    if typ != 'Škoda' and typ != 'Peugeot':
        print('Tento typ auta v půjčovně nemáme.')
    else:
        if typ == 'Škoda':
            if skoda.volne == False:
                stav_tachometru = input('Zadejte stav tachometru: ')
                pocet_dni = int(input('Zadejte pocet dní výpůjčky: '))
                print(skoda.vrat_auto(stav_tachometru,pocet_dni))
            else:
                print('Toto vozidlo nebylo vypůjčeno.')
        else:
            if peugeot.volne == False:
                stav_tachometru = input('Zadejte stav tachometru: ')
                pocet_dni = int(input('Zadejte pocet dní výpůjčky: '))
                print(peugeot.vrat_auto(stav_tachometru, pocet_dni))
            else:
                print('Toto vozidlo nebylo vypůjčeno.')

vypujcka()
vypujcka()
vraceni()
vraceni()


