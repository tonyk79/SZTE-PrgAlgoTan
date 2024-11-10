from collections import deque, defaultdict


def legrövidebb_út_keresése():
    # Adatok beolvasása
    n, m = map(int, input().split())

    # Gráf inicializálása
    gráf = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        gráf[a].append(b)
        gráf[b].append(a)

    # BFS inicializálása
    sor = deque([1])
    távolság = {1: 1}  # Az 1-es csúcsról indulunk, távolság 1 (saját maga)
    előző_csúcs = {1: None}  # Az út visszakövetéséhez

    # BFS ciklus
    while sor:
        csúcs = sor.popleft()

        # Ha elérjük a célt (az n-edik csúcsot), akkor megállunk
        if csúcs == n:
            break

        # Szomszédok bejárása
        for szomszéd in gráf[csúcs]:
            if szomszéd not in távolság:  # Még nem jártunk itt
                távolság[szomszéd] = távolság[csúcs] + 1
                előző_csúcs[szomszéd] = csúcs
                sor.append(szomszéd)

    # Ellenőrizzük, hogy elértük-e az n-edik csúcsot
    if n not in távolság:
        print("IMPOSSIBLE")
        return

    # Útvonal visszakövetése az 1-estől az n-edikig
    útvonal = []
    jelenlegi_csúcs = n
    while jelenlegi_csúcs is not None:
        útvonal.append(jelenlegi_csúcs)
        jelenlegi_csúcs = előző_csúcs[jelenlegi_csúcs]

    útvonal.reverse()  # Az út visszafelé van, így megfordítjuk
    print(távolság[n])  # Az út hossza
    print(" ".join(map(str, útvonal)))  # Az út kiírása


# Függvény hívása
legrövidebb_út_keresése()
