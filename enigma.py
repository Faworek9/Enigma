alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
prze = ['U', 'B', 'C', 'D', 'I', 'F', 'G', 'H', 'E', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'A', 'V',
        'W', 'X', 'Y', 'Z']
przes1 = int(0)
przes2 = int(0)
przes3 = int(0)
przes4 = int(0)
przes5 = int(0)
przes6 = int(0)
lista1 = []
lista2 = []
lista3 = []

alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
pierścień1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A',
              'I', 'B', 'R', 'C', 'J']
pierścień2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P',
              'Y', 'F', 'V', 'O', 'E']
pierścień3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K',
              'M', 'U', 'S', 'Q', 'O']
pierścieńB = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C',
              'W', 'V', 'J', 'A', 'T']
for k in range(przes4):
    z = []
    n = 0
    p = 26
    for v in pierścień1:
        if n == 0:
            n += 1
            z.append(pierścień1[p - 1])
    for y in range(0, p - 1):
        z.append(pierścień1[y])
    pierścień1.clear()
    pierścień1 = z
for k in range(przes5):
    z = []
    n = 0
    p = 26
    for v in pierścień2:
        if n == 0:
            n += 1
            z.append(pierścień2[p - 1])
    for y in range(0, p - 1):
        z.append(pierścień2[y])
    pierścień2.clear()
    pierścień2 = z
for k in range(przes6):
    z = []
    n = 0
    p = 26
    for v in pierścień3:
        if n == 0:
            n += 1
            z.append(pierścień3[p - 1])
    for y in range(0, p - 1):
        z.append(pierścień3[y])
    pierścień3.clear()
    pierścień3 = z

wyraz1 = "AH"
wyrazp = ""
wyrazk = ""
wyrazh = ""
for p in wyraz1:
    wyrazp = wyrazp + prze[alfabet.index(p)]

wyraz1 = wyrazp
for i in wyraz1:
    wyraz2 = ""
    wyraz3 = ""
    wyraz4 = ""
    wyraz5 = ""
    wyraz6 = ""
    wyraz7 = ""
    wyraz8 = ""
    wyraz2 = wyraz2 + pierścień1[alfabet.index(i)]
    wyraz3 = wyraz3 + pierścień2[alfabet.index(wyraz2)]
    wyraz4 = wyraz4 + pierścień3[alfabet.index(wyraz3)]
    wyraz5 = wyraz5 + pierścieńB[alfabet.index(wyraz4)]
    wyraz6 = wyraz6 + alfabet[pierścień3.index(wyraz5)]
    wyraz7 = wyraz7 + alfabet[pierścień2.index(wyraz6)]
    wyraz8 = wyraz8 + alfabet[pierścień1.index(wyraz7)]
    z = []
    n = 0
    p = len(pierścień1)
    for v in pierścień1:
        if n == 0:
            n += 1
            z.append(pierścień1[p - 1])
    for y in range(0, p - 1):
        z.append(pierścień1[y])
    pierścień1.clear()
    pierścień1 = z
    przes2 = przes2 + 1
    z = []
    n = 0
    if przes2 == 26:
        for v in pierścień2:
            if n == 0:
                n += 1
                z.append(pierścień2[p - 1])
        for y in range(0, p - 1):
            z.append(pierścień2[y])
        pierścień2.clear()
        pierścień2 = z
        przes2 = 0
        przes3 = przes3 + 1
    z = []
    n = 0
    if przes3 == 26:
        for v in pierścień3:
            if n == 0:
                n += 1
                z.append(pierścień3[p - 1])
        for y in range(0, p - 1):
            z.append(pierścień3[y])
        pierścień3.clear()
        pierścień3 = z
        przes3 = 0
    wyrazk = wyrazk + wyraz8
for h in wyrazk:
    wyrazh = wyrazh + prze[alfabet.index(h)]
print(wyrazh)


