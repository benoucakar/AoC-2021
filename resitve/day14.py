def dict_add(slov, x, val):
    if x in slov:
        slov[x] += val
    else:
        slov[x] = val

polymer = {}
instructions = {}
switch = True
with open("input/day14.txt") as inp:
    for vrst in inp:
        if vrst == "\n":
            switch = False
            continue
        if switch:
            prvi = vrst[0]
            zadnji = vrst[:-1][-1]
            for i in range(len(vrst)-2):
                dict_add(polymer,vrst[:-1][i:i+2] ,1)
        else:
            temp = vrst[:-1].split(" -> ")
            instructions[temp[0]] = temp[1]

def apply_rules(pari):
    novi_pari = {}
    for (pr,vr) in pari.items():
        if pr in instructions:
            new = instructions[pr]
            dict_add(novi_pari, pr[0]+new, vr)
            dict_add(novi_pari, new+pr[1], vr)
        else:
            dict_add(novi_pari, pr, vr)
    return novi_pari

def main(N):
    poly = polymer.copy()
    for _ in range(N):
        poly = apply_rules(poly)
    score = {}
    for (k,v) in poly.items():
        dict_add(score, k[0], v)
        dict_add(score, k[1], v)
    dict_add(score, prvi, 1)
    dict_add(score, zadnji, 1)
    for (k,v) in score.items():
        score[k] = v//2
    s = sorted(score.values())
    return s[-1]-s[0]

# --------------------------

print("1. del: ")
print(main(10))
print("2. del: ")
print(main(40))