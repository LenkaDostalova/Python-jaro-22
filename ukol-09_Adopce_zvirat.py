import pandas

""" ukol-08: Adopce zvířat
Stáhni si dataset, který obsahuje seznam zvířat k adopci v ZOO Praha. Zdroj dat je Národní katalog otevřených dat.

Data si načti pomocí metody pandas.read_csv(). Pozor, nastav oddělovač na znak středníku. Využij parametr sep.

Seznam se s daty. Kolik má tabulka řádek a sloupců? Jak se sloupce jmenují?

Které zvíře se nachází na záznamu s indexem 34? Vypiš pomocí iloc název tohoto zvířete v češtině i angličtině. """

seznam = pandas.read_csv('dataset.csv',sep=';')
pocet_radku = seznam.shape[0]
pocet_sloupcu = seznam.shape[1]
print(f'\nTabulka zvířat k adopci má {pocet_radku} řádků a {pocet_sloupcu} sloupců.')
print('\nTabulka má tyto sloupce:')
for col in seznam.columns:
    print(f'\t {col}')
print(f'\nNa záznamu s indexem 34 se nachází: {seznam.iloc[34,1]} / {seznam.iloc[34,2]}.\n')

""" Bonus
V lekci jsme zmínili, že existují i jiné typy indexů, než jen číselný, který sám vyrobí pandas. Například v kontextu souboru se zvířaty se nabízí hned několik sloupců, které bychom mohli využít jako index, které nejsou číselné.

Načti znovu data, ale tentokrát nastav parametr index_col na název sloupce, který obsahuje název zvířete v češtině. Všimni si, že sloupec teď povýší na index a už se nenachází mezi "běžnými" sloupci.

Pomocí <tvoje-promenna>.index.is_unique ověř, zda je nový index unikátní.

Seřazený index je efektivnější a přehlednější. Seřaď index pomocí metody .sort_index(). Bacha, metoda vrátí novou tabulku se seřazeným indexem. Budeš tedy chtít přepsat původní tabulku.

Vyhledej řádek indexovaný názvem "Outloň váhavý". Namísto metody .iloc využij .loc.

Rozsahy fungují podobně jako u číselných indexů. Vyhledej záznamy mezi "Želva Smithova" a "Želva žlutočelá". """

seznam_sloupce = pandas.read_csv('dataset.csv',sep=';',index_col='nazev_cz')
#print(seznam_sloupce)
if seznam_sloupce.index.is_unique:
    print('Index je unikátní.')
else:
    print('Index není unikátní.')

seznam_sloupce = seznam_sloupce.sort_index()
#print(seznam_sloupce)
print('\nData o zvířeti Outloň váhavý:')
print(seznam_sloupce.loc['Outloň váhavý'])
print('\nData o zvířatech Želva Smithova až Želva žlutočelá:')
print(seznam_sloupce.loc['Želva Smithova':'Želva žlutočelá'])