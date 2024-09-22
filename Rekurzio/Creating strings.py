def letrehoz(szoveg):
    if len(szoveg) == 0:                             # Alap eset: ha a karakterlánc üres, visszatérünk egy üres listával
        return ['']
    tomb = []                                        # Tömb létrehozása a tárolására

    for i in range(len(szoveg)):                     # Iterálás minden karakteren
        aktualis = szoveg[i]                         # Az aktuális karakter
        maradek = szoveg[:i] + szoveg[i+1:]          # A maradék karakterlánc, ami a permutáció további részét alkotja

        for x in letrehoz(maradek):          # Rekurzióval (letrehoz fgv) generáljuk a maradék karakterlánc permutációit
            tomb.append(aktualis + x)                # Minden permutációhoz hozzáfűzzük az aktuális karaktert

    return tomb

s = input()
minden = letrehoz(s)                                # Generáljuk az összes permutációt
osszes = sorted(set(minden))                 # Kiszűrjük az egyedi permutációkat a set-tel (nem tartalmaz duplikátumot),
                                             # és sorba rendezzük őket a sorted-del (abc szerint)
print(len(osszes))                           # Kiírjuk a permutációk számát
for egyedi in osszes:                        # Kiírjuk az egyedi permutációkat már alfabetikus sorrendben
    print(egyedi)