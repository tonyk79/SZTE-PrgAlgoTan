from collections import deque, defaultdict


def legrovidebb_ut_keresese():
    # Adatok beolvasása
    n, m = map(int, input().split())

    # Gráf inicializálása
    graf = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graf[a].append(b)
        graf[b].append(a)

    # inicializálás (BFS)
    sor = deque([1])
    tavolsag = {1: 1}  # Az 1-es csúcsról indulunk, távolság 1 (saját maga)
    elozo_csucs = {1: None}  # Az út visszakövetéséhez

    # BFS ciklus
    while sor:
        csucs = sor.popleft()

        # Ha elérjük a célt (az n-edik csúcsot), akkor megállunk
        if csucs == n:
            break

        # Szomszédok bejárása
        for szomszed in graf[csucs]:
            if szomszed not in tavolsag:  # Még nem jártunk itt
                tavolsag[szomszed] = tavolsag[csucs] + 1
                elozo_csucs[szomszed] = csucs
                sor.append(szomszed)

    # Ellenőrizzük, hogy elértük-e az n-edik csúcsot
    if n not in tavolsag:
        print("IMPOSSIBLE")
        return

    # Útvonal visszakövetése az 1-estől az n-edikig
    utvonal = []
    jelenlegi_csucs = n
    while jelenlegi_csucs is not None:
        utvonal.append(jelenlegi_csucs)
        jelenlegi_csucs = elozo_csucs[jelenlegi_csucs]

    utvonal.reverse()  # Az út visszafelé van, így megfordítjuk
    print(tavolsag[n])  # Az út hossza
    print(" ".join(map(str, utvonal)))  # Az út kiírása



legrovidebb_ut_keresese()