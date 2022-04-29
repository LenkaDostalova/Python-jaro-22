""" ukol-08: Prodej vstupenek
Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.

Datum	Cena
1. 7. 2021 - 10. 8. 2021	250 Kč
11. 8. 2021 - 31. 8. 2021	180 Kč
Mimo tato data je středisko zavřené.

Tvůj program se nejprve zeptá uživatele na datum a počet osob, pro které uživatel chce vstupenky koupit. Uživatel zadá datum ve středoevropském formátu. Převeď řetězec zadaný uživatelem na datum pomocí funkce datetime.strptime().

Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v té době uzavřené. Pokud je letní kino otevřené, spočítej a vypiš cenu za ubytování.

Data lze porovnávat pomocí známých operátorů <, >, <=, >=, ==, !=. Tyto operátory můžeš použít v podmínce if. Níže vidíš příklad porovnání dvou dat. Program vypíše text "První datum je dřívější než druhé datum.".

from datetime import datetime
prvni_udalost = datetime(2021, 7, 1)
druha_udalost = datetime(2021, 7, 3)
if prvni_datum < druhe_datum:
  print("Druhá událost se stala po první události") """

from datetime import datetime

datum = input('Zadejte datum, na které chcete pořídit vstupenky: ')
date = datetime.strptime(datum, '%d.%m.%Y')
#print(date)

datum_otevreni_kina = datetime(2021,7,1)
datum_zmena_ceny = datetime(2021,8,10)
datum_uzavreni_kina = datetime(2021,8,31)

#pro možnost výpisu otevírací doby ve středoevropském formátu:
oteviraji = datum_otevreni_kina.strftime('%d.%m.%Y') 
zaviraji = datum_uzavreni_kina.strftime('%d.%m.%Y')

cena = 0
pocet_osob = 0

if date < datum_otevreni_kina or date > datum_uzavreni_kina:
    print(f'V tento den je kino uzavřeno. Kino je otevřeno od {oteviraji} do {zaviraji}.')
else:
    pocet_osob = int(input('Zadejte počet vstupenek: '))
    if date <= datum_zmena_ceny:
        cena = 250
    else:
        cena = 180

#print(cena)

celkova_cena = pocet_osob*cena
if celkova_cena != 0:
    print(f'Cena za {pocet_osob} vstupenek je {celkova_cena} Kč.')