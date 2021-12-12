map = []
small = []
with open("input/day12.txt") as inp:
    for vrst in inp:
        temp = sorted(vrst[:-1].split("-"),key=len)
        for c in temp:
            if len(c) <= 2 and c.islower() and c not in small:
                small.append(c)
        if "start" not in temp and "end" not in temp:
            map.append((temp[0],temp[1]))
            map.append((temp[1],temp[0]))
        elif "start" in temp:
            map.append((temp[1],temp[0]))
        elif "end" in temp:
            map.append((temp[0],temp[1]))

def search(pot, fancy_small):
    nove_poti = []
    zadnji = pot[-1]
    for p in [p for p in map if p[0] == zadnji]:
        if p[1] == "end":
            nove_poti += [pot + ["end"]]
        elif p[1] in small:
            if p[1] not in pot:
                nove_poti += search(pot + [p[1]], fancy_small)
            elif p[1] == fancy_small and len([c for c in pot if c == fancy_small]) < 2:
                nove_poti += search(pot + [p[1]], fancy_small)
        else:
            nove_poti += search(pot + [p[1]], fancy_small)
    return nove_poti

podvojene_poti = []
for c in small:
    podvojene_poti += search(["start"], c)
nepodvojene_poti = []
for p in podvojene_poti:
    if p not in nepodvojene_poti:
        nepodvojene_poti.append(p)

# --------------------------

print("1. del: ")
print(len(search(["start"],"")))
print("2. del: ")
print(len(nepodvojene_poti))