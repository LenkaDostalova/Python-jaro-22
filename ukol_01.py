baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod_baliku = input('Zadejte kód balíku:')
if bool(baliky[kod_baliku]) == True:
     print ('Balík byl předán kurýrovi')
else: print ('Balík zatím nebyl předán kurýrovi')