dots = []
folds = []
switch = True
with open("input/day13.txt") as inp:
    for vrst in inp:
        if vrst == "\n":
            switch = False
            continue
        if switch:
            temp = vrst[:-1].split(",")
            dots.append((int(temp[0]),int(temp[1])))
        else:
            temp = vrst[:-1].split(" ")[2].split("=")
            folds.append((temp[0],int(temp[1])))

def folding(tocke, fold):
    nove_tocke = []
    (a, n) = fold
    if a == "x":
        for (x,y) in tocke:
            if x < n:
                nova = (x,y)
            else:
                nova = (2*n-x,y)
            if nova not in nove_tocke:
                nove_tocke.append(nova)
    else:
        for (x,y) in tocke:
            if y < n:
                nova = (x,y)
            else:
                nova = (x,2*n-y)
            if nova not in nove_tocke:
                nove_tocke.append(nova)
    return nove_tocke

dots2 = dots[:]
for fold in folds:
    dots2 = folding(dots2, fold)
sirina = max([b for (_, b) in dots2])
visina = max([a for (a, _) in dots2])
tabela = [[" "]*(visina+1) for _ in range(sirina+1)]
for (x,y) in dots2:
    tabela[y][x] = "0"
#for v in tabela:
#    print(v)

# --------------------------

print("1. del: ")
print(len(folding(dots[:], folds[0])))
print("2. del: ")
print("CPJBERUL")

