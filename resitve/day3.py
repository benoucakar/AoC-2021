diag = []
with open("input/day3.txt") as inp:
    for vrst in inp:
        diag.append(vrst[:-1])

L = len(diag[0])

def cmn_at_indx(sez, i):
    nic = 0
    ena = 0
    for j in range(len(sez)):
        if sez[j][i] == "0":
            nic += 1
        else:
            ena += 1
    if nic > ena:
        return 0
    elif nic < ena:
        return 1
    else:
        return -1

def bin_to_int(niz):
    rniz = niz[::-1]
    num = 0
    for i in range(len(rniz)):
        if rniz[i] == "1":
            num += 2**i
    return num 

def LSR_value(mode):
    kand = diag[:]
    for i in range(L):
        s = cmn_at_indx(kand, i)
        if len(kand) == 1:
            break
        if s == -1:
            m = "1" if mode == "O2" else "0"
            kand = [x for x in kand if x[i]==m]
        else:
            d = str(s) if mode == "O2" else str(1-s)
            kand = [x for x in kand if x[i]==d]
    return bin_to_int(kand[0])

gamma = ""
epsilon = ""
for i in range(L):
    if cmn_at_indx(diag, i) == 0:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"



# --------------------------

print("1. del: ")
print(bin_to_int(gamma)*bin_to_int(epsilon))
print("2. del: ")
print(LSR_value("O2")*LSR_value("CO2"))