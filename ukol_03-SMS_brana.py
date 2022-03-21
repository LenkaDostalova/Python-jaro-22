""" Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:

První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili. Pokud je číslo platné, funkce vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli. """

def phone_number_check (phone_number):
    phone_number = phone_number.replace(' ','')
    if len(phone_number) == 9:
        valid = True
    elif len(phone_number) == 13 and phone_number[0:4] == '+420':
        valid = True
    else:
        valid = False
    return valid

def price (message):
    total_price = 3*(len(message)//180+1)
    return total_price

number = input('Na jaké číslo chcete zprávu zaslat?: ')

if phone_number_check(number) == False:
    print('Chybné telefonní číslo.')
else:
    text = input('Jakou zprávu chcete zaslat?: ')
    print(f'Cena zprávy je: {price(text)} Kč.')