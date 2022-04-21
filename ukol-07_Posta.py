""" ukol-07: Pošta
Česká pošta má stránku na webu, která radí, jak správně nadepsat zásilku. Uvádí i několik vzorů pro české i zahraniční zásilky.

V souboru posta.html nalezneš zdrojový kód této stránky v HTML (to je značkovací jazyk, ve kterém jsou napsané některé webové stránky, nebo části některých webových stránek.).

Soubor si načti do proměnné tak, aby se celý jeho obsah nacházel jako jeden řetězec v proměnné. Můžeš využít metodu read() (doplň název souboru a název své proměnné):
with open(<nazev-souboru>, encoding='utf-8') as vstup:
    <nazev-promenne> = vstup.read()
Nahraď znaky odřádkování (zapisuje se jako '\n') jednoduchou mezerou pomocí metody replace().

Nahraď po sobě jdoucích víc mezer jedinou mezerou: Sestav regulární výraz, který označuje jednu nebo více mezer. Pak pomocí re.sub() nahraď takové sekvence jedinou mezerou. První parametr metody re.sub() je regulární výraz, který nahrazujeme, druhý parametr je řetězec, který nahrazujeme, a třetí parametr je řetězec, ve kterém nahrazujeme.

Příklad použití metody re.sub:

print(re.sub('123?', 'X', 'ABC12ABCD1234'))  # ABCXABCDX4
Najdi v datech všechna česká a slovenská města a jejich PSČ, která se nacházejí v ukázkových adresách. Mají format PSČ MĚSTO, kde PSČ se skládá ze tří číslic, mezery a dvou číslic, a MĚSTO se skládá z jednoho nebo více slov oddělených mezerou, za kterými může ještě následovat číslo pošty.
Například:

460 15 LIBEREC 15
512 11 VYSOKÉ NAD JIZEROU """

import re

nazev_souboru = 'posta.html'
with open(nazev_souboru, encoding='utf-8') as vstup: 
    text = vstup.read() 

#podle zadání takto, ale níže v jednom kroku:
#text = text.replace('\n',' ')
#text = re.sub(' +',' ',text)

text = re.sub('\s+',' ',text)

#print(text)

reg_vyraz_adresa = re.compile('\d{3} \d{2} [\w ]*')
vsechny_adresy = reg_vyraz_adresa.findall(text)

#nektere adresy se opakuji, vytvorim seznam unikatnich adres:
unikatni_adresy = []
for adresa in vsechny_adresy:
    if adresa not in unikatni_adresy:
        unikatni_adresy.append(adresa)

print(f'Celkem nalezeno {len(unikatni_adresy)} unikatních adres:')
for adresa in unikatni_adresy:
    print(adresa)