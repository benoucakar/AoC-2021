img_enhanc_alg = ""
input_img = []
with open("input/day20.txt") as inp:
    flag = True
    for vrst in inp:
        if flag:
            flag = False
            img_enhanc_alg = vrst[:-1]
        elif vrst == "\n":
            continue
        else:
            input_img.append(list(vrst[:-1]))

def bin_to_int(b):
    rb = b[::-1]
    acc = 0
    for i in range(len(b)):
        if rb[i] == "#":
            acc += 2**i
    return acc

def enhance_img(vhod, zz):
    povecan_vhod = []
    povecan_vhod.append([zz]*(len(vhod[0])+4))
    povecan_vhod.append([zz]*(len(vhod[0])+4))
    for vrst in vhod:
        povecan_vhod.append([zz,zz] + vrst + [zz,zz])
    povecan_vhod.append([zz]*(len(vhod[0])+4))
    povecan_vhod.append([zz]*(len(vhod[0])+4))
    izhod = []
    for i in range(1,len(povecan_vhod)-1):
        temp = []
        for j in range(1,len(povecan_vhod[0])-1):
            img_ench_alg_str = povecan_vhod[i-1][j-1] + povecan_vhod[i-1][j] + povecan_vhod[i-1][j+1] + povecan_vhod[i][j-1] + povecan_vhod[i][j] + povecan_vhod[i][j+1] + povecan_vhod[i+1][j-1] + povecan_vhod[i+1][j] + povecan_vhod[i+1][j+1]
            indx = bin_to_int(img_ench_alg_str)
            temp.append(img_enhanc_alg[indx])
        izhod.append(temp)
        temp = []
    return izhod

def povecaj(N):
    znak = "."
    slika = input_img[:]
    for _ in range(N):
        slika = enhance_img(slika, znak)
        if img_enhanc_alg[0] == "#":
            if znak == ".":
                znak = "#"
            else:
                znak = "." 
    count = 0
    for vrst in slika:
        for z in vrst:
            if z == "#":
                count += 1
    return count
    
# --------------------------

print("1. del: ")
print(povecaj(2))
print("2. del: ")
print(povecaj(50))
