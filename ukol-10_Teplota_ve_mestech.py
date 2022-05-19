import requests, pandas
import pytemperature

""" ukol-10: Teplota ve městech
Stáhni si soubor temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.
Dále napiš následující dotazy:
Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? Zde je nápověda.
Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů. """

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/temperature.csv")
open("temperature.csv", "wb").write(r.content)

temperature = pandas.read_csv('temperature.csv')
print(temperature.head())

print('\nPrague:')
print(temperature[temperature['City'] == 'Prague'])
print('No to nebude ve stupních Celsia :-D')

print('\nTeplota vyšší než 80 stupňů:')
dotaz_na_teplotu_80 = temperature['AvgTemperature'] > 80
print(temperature[dotaz_na_teplotu_80])

print('\nTeplota vyšší něž 60 stupňů v Evropě:')
dotaz_na_teplotu_60 = temperature['AvgTemperature'] > 60
dotaz_na_region_Evropa = temperature['Region'] == 'Europe'
print(temperature[dotaz_na_teplotu_60 & dotaz_na_region_Evropa])

print('\nExtrémní teploty:')
dotaz_na_teplotu_minus20 = temperature['AvgTemperature'] < -20
print(temperature[dotaz_na_teplotu_80 | dotaz_na_teplotu_minus20])

""" Bonus
Nainstaluj si modul pytemperature a zkus si vytvořit nový sloupec, který bude obsahovat průměrnou templotu ve stupních Celsia.

Ve svém programu nejprve proveď import modulu pytemperature. Nový sloupec pak přidáš do tabulky tak, že nalevo od = vložíš tabulku a název nového sloupce do hranatých závorek. Napravo pak můžeš provádět výpočty pomocí již existujících sloupců. Můžeš např. použít funkci f2c z modulu pytemperature, která převede teplotu ze stupňů Fahrenheita na stupně Celsia.

import pytemperature
df["AvgTemperatureCelsia"] = pytemperature.f2c(df["AvgTemperature"])
Nyní můžeš zpracovat následující příklady:

Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.
Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů. Jsou některé hodnoty podezřelé? """

temperature['AvgTemperatureinCelsius'] = pytemperature.f2c(temperature['AvgTemperature'])

print('\nTeplota vyšší než 30 stupňů Celsia:')
dotaz_na_teplotu_30C = temperature['AvgTemperatureinCelsius'] > 30
print(temperature[dotaz_na_teplotu_30C])

print('\nTeplota vyšší něž 15 stupňů Celsia v Evropě:')
dotaz_na_teplotu_15C = temperature['AvgTemperatureinCelsius'] > 15
print(temperature[dotaz_na_teplotu_15C & dotaz_na_region_Evropa])

print('\nExtrémní teploty:')
dotaz_na_teplotu_minus10C = temperature['AvgTemperatureinCelsius'] < -10
print(temperature[dotaz_na_teplotu_30C | dotaz_na_teplotu_minus10C])
print('Ano, jsou tam podzřelá data, který by bylo potřeba ověřit.')

""" Bonus 2
Pokračuj ve své práci s informacemi o průměrných teplotách. Pokud jsi zpracoval/a první bonus, můžeš pracovat s teplotami ve stupních Celsia.

Napiš následující dotazy:

Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).
Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec Country hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia. """

print('\nData z 13. listopadu 2017:')
dotaz_na_datum_13 = temperature['Day'] == 13
print(temperature[dotaz_na_datum_13])

print('\nData z 13. listopadu 2017 ve Spojených státech amerických:')
dotaz_na_US = temperature['Country'] == 'US'
temperature_US_13 = temperature[dotaz_na_datum_13 & dotaz_na_US]
print(temperature_US_13)

print('\nData z 13. listopadu 2017, Washington a Philadelphia:')
print(temperature_US_13[temperature_US_13['City'].isin(['Washington','Philadelphia'])])