def make_sNum(niz):
    sNum = []
    for z in niz:
        if z in ["[", "]"]:
            sNum.append(z)
        elif z == ",":
            continue
        else:
            sNum.append(int(z))
    return sNum

def add_sNum(s1, s2):
    return ["["] + s1 + s2 + ["]"]

def explode(s):
    levi_zak = 0 
    for i in range(len(s)):
        if s[i] == "[":
            levi_zak += 1
        if s[i] == "]":
            levi_zak -= 1
        if levi_zak == 5:
            leva_stran = s[:i]
            nL = s[i+1]
            nD = s[i+2]
            desna_stran = s[i+4:]
            for j in range(len(leva_stran)):
                if isinstance(leva_stran[len(leva_stran) - 1 - j], int):
                    leva_stran[len(leva_stran) - 1 - j] += nL
                    break
            for j in range(len(desna_stran)):
                if isinstance(desna_stran[j], int):
                    desna_stran[j] += nD
                    break
            return leva_stran + [0] + desna_stran
    return None

def split(s):
    for i in range(len(s)):
        if s[i] not in ["[", "]"]:
            if s[i] >= 10:
                leva_stran = s[:i]
                nL = s[i] // 2
                nD = (s[i] + 1)// 2 
                desna_stran = s[i+1:]
                return leva_stran + ["[", nL, nD, "]"] + desna_stran
    return None

def reduce(s):
    reduced = s[:]
    while True:
        exploded = explode(reduced)
        if exploded != None:
            reduced = exploded[:]
        else:
            splitted = split(reduced)
            if splitted == None:
                return reduced
            else:
                reduced = splitted[:]


sNumbers = []
with open("input/day18.txt") as inp:
    for vrst in inp:
        sNumbers.append(make_sNum(vrst[:-1]))

vsota = sNumbers[0]
for s in sNumbers[1:]:
    vsota = add_sNum(vsota, s)
    vsota = reduce(vsota)

def magnitude(S):
    def helper(s):
        for i in range(len(s)):
            if isinstance(s[i], int) and isinstance(s[i+1], int):
                leva_stran = s[:i-1]
                desna_stran = s[i+3:]
                return leva_stran + [3*s[i] + 2*s[i+1]] + desna_stran
    while len(S) > 1:
        S = helper(S)
    return S[0]

print(magnitude(vsota))

max_mag = 0
for s1 in sNumbers:
    for s2 in sNumbers:
        if s1 == s2:
            continue
        max_mag = max(max_mag, magnitude(reduce(add_sNum(s1, s2))))
print(max_mag)