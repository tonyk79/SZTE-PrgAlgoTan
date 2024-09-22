def nullaig(n):
    lepesek = 0
    while n > 0:                                         #Amíg nullág el nem érünk
        legnagyobb = max(int(szam) for szam in str(n))   # max-al kivesszük a legnagyobb számot az iterált számjegyek közül
        n -= legnagyobb
        lepesek += 1
    return lepesek

n = int(input())
print(nullaig(n))


