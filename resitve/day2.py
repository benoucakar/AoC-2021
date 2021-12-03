ukazi = []
with open("input/day2.txt") as inp:
    for vrst in inp:
        ukaz = vrst.split()
        ukazi.append((ukaz[0],int(ukaz[1])))

hor1 = 0
dpth1 = 0
for par in ukazi:
    if par[0] == 'forward':
        hor1 += par[1]
    elif par[0] == 'up':
        dpth1 -= par[1]
    elif par[0] == 'down':
        dpth1 += par[1]

hor2 = 0
dpth2 = 0
aim2 = 0
for par in ukazi:
    if par[0] == 'forward':
        hor2 += par[1]
        dpth2 += aim2 * par[1]
    elif par[0] == 'up':
        aim2 -= par[1]
    elif par[0] == 'down':
        aim2 += par[1] 

# --------------------------

print("1. del: ")
print(hor1 * dpth1)
print("2. del: ")
print(hor2 * dpth2)