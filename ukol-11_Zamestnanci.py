import requests, pandas

""" ukol-11: Zaměstnanci a Projekty
Zaměstnanci
Uvažuj, že zpracováváš analýzu pro softwarovou firmu. Firma má kanceláře v Praze, Plzni a Liberci. Seznam zaměstnanců pro jednotlivé kanceláře najdeš v souborech zam_praha.csv, zam_plzeň.csv a zam_liberec.csv.

Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame). Ke každé tabulce přidej nový sloupec mesto, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.
Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to, že v naší firmě již nepracuje.
Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.

Dobrovolný doplněk

Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.
V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují. Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují. Tabulku ulož do souboru CSV.
Projekty
Pokračuj ve své práci pro softwarovou firmu. Ze souboru vykazy.csv načti informace o výkazech na projekty pro jednoho vybraného zákazníka.

Načti data ze souboru a ulož je do tabulky.
Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.
Dobrovolný doplněk

Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení.

Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře, tj. spočítej celkový počet hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka. """

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_praha.csv")
open("zam_praha.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_plzeň.csv")
open("zam_plzeň.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_liberec.csv")
open("zam_liberec.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
open("platy_2021_02.csv", "wb").write(r.content)

zam_Praha = pandas.read_csv('zam_praha.csv')
zam_Praha['mesto'] = 'Praha'

zam_Plzen = pandas.read_csv('zam_plzeň.csv')
zam_Plzen['mesto'] = 'Plzeň'

zam_Liberec = pandas.read_csv('zam_liberec.csv')
zam_Liberec['mesto'] = 'Liberec'

zamestnanci = pandas.concat([zam_Praha,zam_Plzen, zam_Liberec], ignore_index=True)

platy = pandas.read_csv('platy_2021_02.csv')
zamestnanci_platy = pandas.merge(zamestnanci,platy, on='cislo_zamestnance', how='outer')

print(f'Po sloučení má tabulka {zamestnanci_platy.shape[0]} záznamů, před sloučením měla {zamestnanci.shape[0]} záznamů.')

print('\nPrůměrný plat na pobočkách:')
print(zamestnanci_platy.groupby('mesto')['plat'].mean())

pocet_nepracujicich = zamestnanci_platy[zamestnanci_platy['plat'].isnull()].shape[0]
nepracujici = zamestnanci_platy[zamestnanci_platy['plat'].isnull()]
nepracujici = nepracujici[['jmeno','prijimeni']]
nepracujici.to_csv('nepracujici.csv', index = False)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/vykazy.csv")
open("vykazy.csv", "wb").write(r.content)
vykazy = pandas.read_csv('vykazy.csv')

celkem_vykazano_hodin = vykazy['hours'].sum()
print(f'\nCelkový počet vykázaných hodin za jednotlivé projekty: {celkem_vykazano_hodin}')

zamestnanci_projekty = pandas.merge(zamestnanci,vykazy, left_on='cislo_zamestnance', right_on='emloyee_id')
print('Vykázané hodiny podle kanceláří:')
print(zamestnanci_projekty.groupby('mesto')['hours'].sum())