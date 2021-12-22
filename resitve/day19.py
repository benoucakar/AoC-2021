import heapq

scanner_data = []
with open("input/day19.txt") as inp:
    flag = True
    temp = []
    for vrst in inp:
        if flag:
            flag = False
        elif vrst == "\n":
            scanner_data.append(temp)
            temp = []
            flag = True
        else:
            s = vrst[:-1].split(",")
            temp.append((int(s[0]), int(s[1]), int(s[2])))
    scanner_data.append(temp)

def apply_rotacija(t, rot):
    ix, iy, iz, px, py, pz = rot
    return ((t[ix]*px, t[iy]*py, t[iz]*pz))

rotacije = []
for p in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 1, 0), (2, 0, 1)]:
    for z in [(1, 1, 1), (-1, 1, 1), (1, -1, 1), (1, 1, -1), (-1, -1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, -1)]:
        e1 = apply_rotacija((1, 0, 0), (p[0], p[1], p[2], z[0], z[1], z[2]))
        e2 = apply_rotacija((0, 1, 0), (p[0], p[1], p[2], z[0], z[1], z[2]))
        e3 = apply_rotacija((0, 0, 1), (p[0], p[1], p[2], z[0], z[1], z[2]))
        e3_ = (e1[1]*e2[2]-e1[2]*e2[1], -e1[0]*e2[2] +
               e1[2]*e2[0], e1[0]*e2[1]-e1[1]*e2[0])
        if e3 == e3_:
            rotacije.append((p[0], p[1], p[2], z[0], z[1], z[2]))

def je_sosed(scnr1, scnr2):
    for r in rotacije:
        rotated = list(map(lambda t: apply_rotacija(t, r), scnr2))
        vectors = []
        for s1 in scnr1:
            for s2 in rotated:
                vectors.append((s1[0]-s2[0], s1[1]-s2[1], s1[2]-s2[2]))
        stevec = {}
        for v in vectors:
            if v in stevec:
                stevec[v] += 1
                if stevec[v] >= 12:
                    return (r, v)
            else:
                stevec[v] = 1
    return (None, None)

# BFS
queue = [0]
visited = [False]*len(scanner_data)
visited[0] = True
polozaji = [None]*len(scanner_data)
polozaji[0] = (0, 0, 0)
heapq.heapify(queue)
while len(queue) > 0:
    scnr_indx = heapq.heappop(queue)
    for i in range(len(scanner_data)):
        r, v = je_sosed(scanner_data[scnr_indx], scanner_data[i])
        if r is not None and not visited[i]:
            scanner_data[i] = list(
                map(lambda t: apply_rotacija(t, r), scanner_data[i]))
            visited[i] = True
            polozaji[i] = (polozaji[scnr_indx][0] + v[0], polozaji[scnr_indx]
                           [1] + v[1], polozaji[scnr_indx][2] + v[2])
            heapq.heappush(queue, i)

beacons = set()
for i in range(len(scanner_data)):
    for beacon in scanner_data[i]:
        beacons.add((polozaji[i][0] + beacon[0], polozaji[i]
                     [1] + beacon[1], polozaji[i][2] + beacon[2]))

def manhattan(t1, t2):
    x1, y1, z1 = t1
    x2, y2, z2 = t2
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

# --------------------------

print("1. del: ")
print(len(beacons))
print("2. del: ")
print(max([manhattan(t1, t2) for t1 in polozaji for t2 in polozaji]))
