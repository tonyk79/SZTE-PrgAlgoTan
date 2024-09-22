# Remove digits

A feldataban kérjünk be egy számot és jussunk el nulláig úgy, hogy a megadott számból csak a szám egyik számjegyét vonhatjuk ki.

Mennyi a minimális lépések száma?

# Bemenet

Az egytetlen bemeneti érték egy szám.

# Kiment

Az egyetlen kimeneti érték a minimális lépések száma.

# Megkötések

-   $1 \le n \le  10^6$

# Példa

Bemenet:
27

Kimenet:
5

Magyarázat: 
27→20→18→10→9→0
Az optimális megoldáshoz, mindig a legnagyobb számjegyet vonuk ki. 27-es számból vonjuk ki a 7-et → 20
20-ból vonjuk ki a 2-est → 18
18-ból vonjuk ki a 8-ast → 10
10-ből vonjuk ki az 1-et → 9 
9-ből vonjuk ki a 9-et → 0


