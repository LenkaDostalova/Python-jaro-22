""" Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa. Služba nabízí dva typy pořadů - filmy a seriály. Firma chce evidovat, které filmy a seriály nabízí a jejich žánry. Dále chce u filmů evidovat délku a u seriálů počet episod a délku jedné episody.

Vytvoř program, který bude obsahovat tři třídy - Polozka, Film a Serial.
Třída Polozka bude sloužit jako základ pro další třídy. Bude mít atributy určující název a žánr. Oba atributy nastav ve funkci __init__ a získej je jako parametry.
Třída Film bude potomkem třídy Polozka. Film má kromě názvu a žánru atribut délka.
Třída Serial bude potomkem třídy Polozka. Má kromě názvu a žánru atributy počet epizod a délka epizody.
Všem třídám přidej funkci get_info, která vypíše informace o položce, resp. o filmu a seriálu. Funkce u třídy Polozka vypíše název a žánr. Následně tuto funkci využij ve funkcích u tříd Film a Serial a přidej k ní informaci o délce, resp. počtu episod.
Po naprogramování si vytvoř alespoň jeden objekt reprezentující film a seriál a ověř, že vše funguje. 

Bonus:
Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají. Vytvoř třídu Uzivatel, která bude mít atributy uzivatelske_jmeno a delka_sledovani, který udává celkovou délku pořadů, které uživatel zhlédl. Uživatelské jméno získej jako parametr a délka sledování je na začátku 0.

Třídám Serial a Film přidej funkci get_celkova_delka, která vrátí celkovou délku filmu/seriálu (u seriálu je to počet episod násobený délkou jedné episody).

Třídě Uzivatel přidej funkci pripocti_zhlednuti, která bude mít jeden parametr. Funkce zvýší atribut udávající celkovou délku sledávní o zadaný parametr.

Vytvoř objekt, který reprezentuje nějakého uživatele. Následně zkus uvažovat situaci, že uživatel zhlédne film a seriál, které jsi vytvořil(a) jako objekty. Uživateli připočti délky děl k délce sledování, využij k tomu funkci get_celkova_delka u objektu a seriálu, abys zjistil(a), kolik minut (nebo hodin) videa celkem uživatel zhlédl.

Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné a tuto pomocnou proměnnou potom předáš jako parametr funkci pripocti_zhlednuti."""

class Polozka:
    def __init__(self,nazev,zanr):
        self.nazev = nazev
        self.zanr = zanr
    def get_info(self):
        return f'{self.nazev} je žánru {self.zanr}.'

class Film(Polozka):
    def __init__(self,nazev,zanr,delka):
        super().__init__(nazev,zanr)
        self.delka = int(delka)
    def get_info(self):
        return ('Film ' + super().get_info() + f' Délka filmu je {self.delka} minut.')
    def get_celkova_delka(self):
        return self.delka

class Serial(Polozka):
    def __init__(self,nazev,zanr,pocet_epizod,delka_epizody):
        super().__init__(nazev,zanr)
        self.pocet_epizod = int(pocet_epizod)
        self.delka_epizody = int(delka_epizody)
    def get_info(self):
        return ('Seriál ' + super().get_info() + f' Seriál má {self.pocet_epizod} epizod a každá epizoda má délku {self.delka_epizody} minut.')
    def get_celkova_delka(self):
        return self.pocet_epizod * self.delka_epizody

class Uzivatel:
    def __init__(self,uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0
    def pripocti_zhlednuti(self,delka_zhlednuti):
        self.delka_sledovani += delka_zhlednuti

pupendo = Film('Pupendo','komedie',120)
print(pupendo.get_info())

rapl = Serial('Rapl','krimi',26,60)
print(rapl.get_info())

lenka = Uzivatel('Lenka')
#print(lenka.delka_sledovani)
lenka.pripocti_zhlednuti(pupendo.get_celkova_delka())
#print(lenka.delka_sledovani)
lenka.pripocti_zhlednuti(rapl.get_celkova_delka())
print(f'Uživatel {lenka.uzivatelske_jmeno} sledoval naše pořady celkem {lenka.delka_sledovani} minut.')