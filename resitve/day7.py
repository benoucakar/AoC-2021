inp = open("input/day7.txt", "r")
prvotni_polozaji = [int(x) for x in inp.readline().split(",")]
inp.close()

M = max(prvotni_polozaji)

def ocenjevanje1(n):
    return n

def ocenjevanje2(n):
    return n*(n+1)//2

def crab_commander(ocenjevanje):
    cene = []
    for p in range(M+1):
        temp_cena = 0
        for crab in prvotni_polozaji:
            temp_cena += ocenjevanje(abs(p - crab))
        cene.append(temp_cena)
    return min(cene)

# --------------------------

print("1. del: ")
print(crab_commander(ocenjevanje1))
print("2. del: ")
print(crab_commander(ocenjevanje2))