inp = open("input/day6.txt", "r")
prvotne_ribe = [int(x) for x in inp.readline().split(",")]
inp.close()

prvotna_populacija = [0 for _ in range(9)]
for riba in prvotne_ribe:
    prvotna_populacija[riba] += 1

def zivljenje(N):
    populacija = prvotna_populacija
    for _ in range(N):
        nova_populacija = [0 for _ in range(9)]
        for k in range(9):
            if k == 0:
                nova_populacija[8] += populacija[k]
                nova_populacija[6] += populacija[k]
            else:
                nova_populacija[k-1] += populacija[k]
        populacija = nova_populacija
    return sum(populacija)

# --------------------------

print("1. del: ")
print(zivljenje(80))
print("2. del: ")
print(zivljenje(256))


