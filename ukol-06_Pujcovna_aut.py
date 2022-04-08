""" ukol-06: Půjčovna aut
Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

Napište program, který na výstup vypíše součet všech ujetých kilometrů. 

Upravte váš program tak, aby jméno souboru k otevření zadal uživatel, abychom mohli takto zpracovávat výkazy z různých souborů, aniž bychom museli upravovat samotný kód programu. Program ověřte tak, že si soubor auta.txt přejmenujete, nebo si vytvořte nový."""

nazev_souboru = input('Zadejte název souboru: ')
with open(nazev_souboru, encoding='utf-8') as vstup: 
    auta = vstup.readlines() 

auta = [auto.split() for auto in auta]
#print(auta)

najeto_km = [float(auto[1].replace(',','.')) for auto in auta]
#print(sum(najeto_km))

print(f'Součet všech ujetých kilometrů je: {sum(najeto_km)} tisíc kilometrů.')