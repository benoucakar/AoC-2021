map = []
with open("input/day9.txt") as inp:
    for vrst in inp:
        map.append([int(x) for x in vrst[:-1]])
bmap = [[10]*(len(map[0])+2)] + [[10] + map[i] + [10] for i in range(len(map))] + [[10]*(len(map[0])+2)]

low_points = []
for i in range(1,len(bmap)-1):
    for j in range(1,len(bmap[0])-1):
        if bmap[i][j] < bmap[i+1][j] and bmap[i][j] < bmap[i-1][j] and bmap[i][j] < bmap[i][j+1] and bmap[i][j] < bmap[i][j-1]:
            low_points.append((i,j))

def basin_size(low_point):
    basin = []
    cand = [low_point]
    while len(cand) > 0:
        (a,b) = cand[0]
        to_check = [(a-1,b), (a+1,b), (a,b-1), (a,b+1)]
        for (i,j) in to_check:
            if (i,j) not in basin and (i,j) not in cand and bmap[i][j] < 9:
                cand.append((i,j))
        cand.remove((a,b))
        basin.append((a,b))
    return len(basin)

basin_sizes = sorted([basin_size(p) for p in low_points], reverse=True)

# --------------------------

print("1. del: ")
print(sum([bmap[i][j] for (i,j) in low_points]) + len(low_points))
print("2. del: ")
print(basin_sizes[0]*basin_sizes[1]*basin_sizes[2])
    