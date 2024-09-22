def min_ktsg(n, hosszok):
    hosszok.sort()                  # Rendezés
    median = hosszok[n // 2]        # Medián megahtározása -> a rendezett adathalmaz középső eleme

    ossz_ktsg = sum(abs(hossz - median) for hossz in hosszok)     # Összköltség kiszámítása abszolutértékkel (abs)

    return ossz_ktsg

                                            # Bemenetek olvasása
n = int(input())                            # 5
hosszok = list(map(int, input().split()))  # 2 3 1 5 2  -> 1,2,2,3,5 -> med.: 2
                                            #split szóközök mentén darabol
                                            #map fgv. egy adott fgv-t (int) alkalmaz minden elemre, azaz számmá alakít
                                            #list() iterálható objekt. visszaadása

                                            # Eredmény kiírása
print(min_ktsg(n, hosszok))                 # Kimenet: 5
