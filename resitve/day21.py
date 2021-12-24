from functools import lru_cache

with open("input/day21.txt") as inp:
    temp = []
    for vrst in inp:
        temp.append(int(vrst[28:-1]))
    p1_start = temp[0]
    p2_start = temp[1]

def igra1():
    def det_dice(kocka):
            if kocka == 100:
                return 1
            else:
                return kocka + 1 
    p1 = p1_start - 1
    p2 = p2_start - 1
    p1_points = 0
    p2_points = 0
    rolls = 0
    dice = 1
    while True:
        # Prvi igralec
        p1_move = 0
        for _ in range(3):
            p1_move += dice
            dice = det_dice(dice)
        p1 = (p1 + p1_move) % 10
        p1_points += p1 + 1
        rolls += 3
        if p1_points >= 1000:
            return rolls * p2_points
        # Drugi igralec
        p2_move = 0
        for _ in range(3):
            p2_move += dice
            dice = det_dice(dice)
        p2 = (p2 + p2_move) % 10
        p2_points += p2 + 1
        rolls += 3
        if p2_points >= 1000:
            return rolls * p1_points
        
dirac = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
@lru_cache(maxsize=None)
def igra2(p1,p2,p1_points,p2_points,igralec,dir_val):
    if igralec == "prvi":
        p1n = (p1 + dir_val) % 10
        p1n_points = p1_points + p1n + 1
        if p1n_points >= 21:
            return (1,0)
        else:
            p1_vesolja = 0
            p2_vesolja = 0
            for par in dirac.items():
                k,v = par
                p1_ves, p2_ves = igra2(p1n, p2, p1n_points, p2_points, "drugi", k)
                p1_vesolja += v * p1_ves
                p2_vesolja += v * p2_ves
            return (p1_vesolja, p2_vesolja)
    else:
        p2n = (p2 + dir_val) % 10
        p2n_points = p2_points + p2n + 1
        if p2n_points >= 21:
            return (0, 1)
        else:
            p1_vesolja = 0
            p2_vesolja = 0
            for par in dirac.items():
                k,v = par
                p1_ves, p2_ves = igra2(p1, p2n, p1_points, p2n_points, "prvi", k)
                p1_vesolja += v * p1_ves
                p2_vesolja += v * p2_ves
            return (p1_vesolja, p2_vesolja)
        
p1_vesolja = 0
p2_vesolja = 0
for par in dirac.items():
    k,v = par
    p1_ves, p2_ves = igra2(p1_start - 1, p2_start - 1, 0, 0, "prvi", k)
    p1_vesolja += v * p1_ves
    p2_vesolja += v * p2_ves

# --------------------------

print("1. del: ")
print(igra1())
print("2. del: ")
print(max(p1_vesolja,p2_vesolja))