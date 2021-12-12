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

def ze_v_poti(p, pot):
    if len(pot) < 2:
        return False
    else:
        for i in range(len(pot)-1):
            if p == (pot[i],pot[i+1]):
                return True
        return False

def search1(pot):
    nove_poti = []
    zadnji = pot[-1]
    for p in [p for p in map if p[0] == zadnji]:
        if ze_v_poti(p, pot):
            continue
        if p[1] == "end":
            nove_poti += [pot + ["end"]]
        elif p[1] in small:
            if p[1] not in pot:
                nove_poti += search1(pot + [p[1]])
        else:
            nove_poti += search1(pot + [p[1]])
    return nove_poti

#print(len(search1(["start"])))

def search2(pot, fancy_small):
    nove_poti = []
    zadnji = pot[-1]
    for p in [p for p in map if p[0] == zadnji]:
        #if ze_v_poti(p, pot):
            #continue
        if p[1] == "end":
            nove_poti += [pot + ["end"]]
        elif p[1] in small:
            if p[1] not in pot:
                nove_poti += search2(pot + [p[1]], fancy_small)
            elif p[1] == fancy_small and len([c for c in pot if c == fancy_small]) < 2:
                nove_poti += search2(pot + [p[1]], fancy_small)
        else:
            nove_poti += search2(pot + [p[1]], fancy_small)
    return nove_poti

#podvojene_poti = []
#for c in small:
#    podvojene_poti += search2(["start"], c)
#nepodvojene_poti = []
#for p in podvojene_poti:
#    if p not in nepodvojene_poti:
#        nepodvojene_poti.append(p)
#print(len(nepodvojene_poti))

print(len(search2(["start"],"")))