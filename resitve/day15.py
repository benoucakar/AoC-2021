import heapq

def make_map(n):
    map = []
    for i in range(n):
        with open("input/day15.txt") as inp:
            for vrst in inp:
                temp = []
                for j in range(n):
                    for z in vrst[:-1]:
                        temp.append(((int(z) + i + j - 1) % 9) + 1)
                map.append(temp)
    return map

def dijkstra(map):
    visina = len(map)
    sirina = len(map[0])
    visited = [[False]*sirina for _ in range(visina)]
    cost = [[float("inf")]*sirina for _ in range(visina)]
    cost[0][0] = 0
    heap = [(0,0,0)] # (cena, i, j)
    heapq.heapify(heap)

    while len(heap) > 0:
        cena, i, j = heapq.heappop(heap)
        if visited[i][j]:
            continue
        visited[i][j] = True
        for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
            a = i + x
            b = j + y
            if not (0 <= a < visina and 0 <= b < sirina):
                continue
            if visited[a][b]:
                continue
            if cost[a][b] > cost[i][j] + map[a][b]:
                cost[a][b] = cost[i][j] + map[a][b]
                heapq.heappush(heap, (cost[a][b],a,b))
    return cost[-1][-1]

# --------------------------

print("1. del: ")
print(dijkstra(make_map(1)))
print("2. del: ")
print(dijkstra(make_map(5)))