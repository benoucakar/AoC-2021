import re

data = []
with open("input/day5.txt") as inp:
    for vrst in inp:
        vzorec = re.compile(r'(?P<x1>(\d*)),(?P<y1>(\d*)) -> (?P<x2>(\d*)),(?P<y2>(\d*))')
        x1 = int(vzorec.search(vrst).group("x1"))
        y1 = int(vzorec.search(vrst).group("y1"))
        x2 = int(vzorec.search(vrst).group("x2"))
        y2 = int(vzorec.search(vrst).group("y2"))
        data.append((x1,y1,x2,y2))

hor_vert = []
for d in data:
    if d[0] == d[2] or d[1] == d[3]:
        hor_vert.append(d)

def tocke_iz_crte(d):
    tocke = []
    (x1,y1,x2,y2) = d
    if x1 == x2:
        Y1 = min(y1,y2)
        Y2 = max(y1,y2)
        while Y1 <= Y2:
            tocke.append((x1,Y1))
            Y1 += 1
        return tocke
    if x1 < x2:
        (X1,Y1,X2,Y2) = (x1,y1,x2,y2)
    else:
        (X1,Y1,X2,Y2) = (x2,y2,x1,y1)
    k = (Y2 - Y1) // (X2 - X1)
    while X1 <= X2:
        tocke.append((X1,Y1))
        X1 += 1
        Y1 += k
    return tocke

def napolni_svet(podatki):
    svet = {}
    for d in podatki:
        tocke = tocke_iz_crte(d)
        for t in tocke:
            if t in svet:
                svet[t] += 1
            else:
                svet[t] = 1
    return svet

vred1 = sum(1 for n in napolni_svet(hor_vert).values() if n >= 2)
vred2 = sum(1 for n in napolni_svet(data).values() if n >= 2)

print("1. del: ")
print(vred1)
print("2. del: ")
print(vred2)
