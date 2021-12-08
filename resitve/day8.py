patterns = []
outputs = []
with open("input/day8.txt") as inp:
    for vrst in inp:
        vrst_splt = vrst.split()
        meja = vrst_splt.index("|") 
        patterns.append(vrst_splt[:meja])
        outputs.append(vrst_splt[meja+1:])

L = len(patterns)
crke = {"a","b","c","d","e","f","g",}

count = 0
for sez in outputs:
    for code in sez:
        if len(code) in [2,3,4,7]:
            count += 1

# - 0 -
# 1   2
# - 3 -
# 4   5
# - 6 -

def decode(pattern, output):
    spomin = [""]*7
    ena = set([p for p in pattern if len(p) == 2][0])
    stiri = set([p for p in pattern if len(p) == 4][0])
    sedem = set([p for p in pattern if len(p) == 3][0])
    # Določimo položaj 0
    spomin[0] = (sedem - ena).pop()
    # Določimo položaja 2 in 5
    manjka_ena = [set(p) for p in pattern if len(p) == 6]
    for e in manjka_ena:
        if not ena.issubset(e):
            spomin[2] = (ena - e).pop()
            spomin[5] = (ena - {spomin[2],}).pop()
            manjka_ena.remove(e)
    # Določimo položaja 1 in 3
    stiri_brez_25 = stiri - ena
    for e in manjka_ena:
        if not stiri_brez_25.issubset(e):
            spomin[3] = (stiri_brez_25 - e).pop()
            spomin[1] = (stiri_brez_25 - {spomin[3],}).pop()
            manjka_ena.remove(e)
    # Določimo položaja 4 in 6
    spomin[6] = (manjka_ena[0] - stiri - sedem).pop()
    spomin[4] = (crke - manjka_ena[0]).pop()
    
    slovar = {
        "".join(sorted([spomin[i] for i in [2,5]])): 1, 
        "".join(sorted([spomin[i] for i in [0,2,3,4,6]])): 2,
        "".join(sorted([spomin[i] for i in [0,2,3,5,6]])): 3,
        "".join(sorted([spomin[i] for i in [1,2,3,5]])): 4,
        "".join(sorted([spomin[i] for i in [0,1,3,5,6]])): 5,
        "".join(sorted([spomin[i] for i in [0,1,3,4,5,6]])): 6,
        "".join(sorted([spomin[i] for i in [0,2,5]])): 7,
        "".join(sorted([spomin[i] for i in [0,1,2,3,4,5,6]])): 8,
        "".join(sorted([spomin[i] for i in [0,1,2,3,5,6]])): 9,
        "".join(sorted([spomin[i] for i in [0,1,2,4,5,6]])): 0
    }

    rez = 0
    for e in output:
        rez *= 10
        rez += slovar["".join(sorted(e))]
    
    return rez

# --------------------------

print("1. del: ")
print(count)
print("2. del: ")
print(sum([decode(patterns[i], outputs[i]) for i in range(L)]))