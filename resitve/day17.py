import re

inp = open("input/day17.txt", "r")
vzorec = re.compile(r'.*x=(?P<x1>(.*))\.\.(?P<x2>(.*)), y=(?P<y1>(.*))\.\.(?P<y2>(.*))')
vrst = inp.readline()[:-1]
x1 = int(vzorec.search(vrst).group("x1"))
y1 = int(vzorec.search(vrst).group("y1"))
x2 = int(vzorec.search(vrst).group("x2"))
y2 = int(vzorec.search(vrst).group("y2"))
inp.close()

N = 200
sez = []
for vx0 in range(N):
    for vy0 in range(-N, N):
        flag = True
        vx = vx0
        vy = vy0
        x = 0
        y = 0
        max_y = y
        while flag:
            x = x + vx
            y = y + vy
            if vx > 0:
                vx -= 1
            elif vx < 0:
                vx += 1
            vy -= 1
            max_y = max(y, max_y)
            if x1 <= x <= x2 and y1 <= y <= y2:
                sez.append((vx0,vy0,max_y))
                flag = False
            else:
                if x < x1 and vx <= 0:
                    flag = False
                elif x > x2 and vx >= 0:
                    flag = False
                elif y < y1 and vy <= 0:
                    flag = False

# --------------------------

print("1. del: ")
print(max([t[2] for t in sez]))
print("2. del: ")
print(len(sez))