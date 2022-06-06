import requests, pandas
import matplotlib.pyplot as plt

""" Histogram platů
Stáhni si soubor platy_2021_02.csv s informacemi o platech v softwarové firmě.
Načti si tato data do tabulky a vytvoř histogram. Nastav vhodně hranice skupin histogramu (parametr bins), aby byl graf přehledný a snadno interpretovatelný.
 """

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
open("platy_2021_02.csv", "wb").write(r.content)

platy = pandas.read_csv('platy_2021_02.csv')

platy.hist(column='plat', bins=[25000,30000,35000,40000,45000,50000,55000,60000,65000])
plt.show()

""" Dobrovolný doplněk
Vyzkoušej si vytvořit podgrafy. pandas a matplotlib to umí poměrně jednoduše a to pomocí parametru by metody hist(). Jako parametr vlož sloupec, podle kterého chceš data do podgrafů rozdělit. Musíš vložit sloupec ve formě dat, nikoli pouze jeho název.

Vytvoř pro zadaná data podgrafy pro jednotlivá města. Načti si informace o městě, ve kterém jednotliví pracovníci pracují (to jsme již dělali v minulém úkolu). Následně sloupec mesto použij na rozdělení podgrafů.

Příklad výstupu je na obrázku níže. """

zam_Praha = pandas.read_csv('zam_praha.csv')
zam_Praha['mesto'] = 'Praha'

zam_Plzen = pandas.read_csv('zam_plzeň.csv')
zam_Plzen['mesto'] = 'Plzeň'

zam_Liberec = pandas.read_csv('zam_liberec.csv')
zam_Liberec['mesto'] = 'Liberec'

zamestnanci = pandas.concat([zam_Praha,zam_Plzen, zam_Liberec], ignore_index=True)
zamestnanci_platy = pandas.merge(zamestnanci,platy, on='cislo_zamestnance', how='outer')

zamestnanci_platy.hist(column='plat', bins=[25000,30000,35000,40000,45000,50000,55000,60000,65000], by='mesto')
plt.show()

""" Teplota ve městech
Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.
Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech.
 """

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/temperature.csv")
open("temperature.csv", "wb").write(r.content)

teplota = pandas.read_csv('temperature.csv')

dotaz_na_mesta = teplota['City'].isin(['Helsinki','Miami Beach','Tokyo'])
teplota_ve_vybranych_mestech = teplota[dotaz_na_mesta]

teplota_ve_vybranych_mestech.plot.box(column='AvgTemperature', by='City')
plt.show()