octopy = []
with open("input/day11.txt") as inp:
    for vrst in inp:
        octopy.append(list(map(int,list(vrst[:-1]))))

def matrix_max(A):
    max_vrst = [max(vrst) for vrst in A]
    M = max(max_vrst)
    i = max_vrst.index(M)
    j = A[i].index(M)
    return (i,j)    

def update(octp, flashes):
    tired_octpy = [[False]*10 for _ in range(10)]
    # 1. korak: Povečaš energijo vseh za 1
    for i in range(10):
        for j in range(10):
            octp[i][j] += 1
    # 2. korak: Hobotnice svetijo in se resetirajo na 0
    (Mi,Mj) = matrix_max(octp)
    while octp[Mi][Mj] > 9:
        flashes += 1
        kand = [
        (i,j) for (i,j) in
        [(Mi+1,Mj+1),(Mi,Mj+1),(Mi-1,Mj+1),(Mi+1,Mj),(Mi-1,Mj),(Mi+1,Mj-1),(Mi,Mj-1),(Mi-1,Mj-1)] 
        if 0 <= i <= 9 and 0 <= j <= 9
        ]
        for (i,j) in kand:
            if not tired_octpy[i][j]:
                octp[i][j] += 1
        tired_octpy[Mi][Mj] = True
        octp[Mi][Mj] = 0
        (Mi,Mj) = matrix_max(octp)
    return (octp, flashes)

octo_copy1 = [vrst[:] for vrst in octopy]
total_flashes = 0
for _ in range(100):
    (octo_copy1, total_flashes) = update(octo_copy1, total_flashes)

octo_copy2 = [vrst[:] for vrst in octopy]
flashes_at_once = 0
step = 0
while flashes_at_once < 100:
    (octo_copy2, flashes_at_once) = update(octo_copy2, 0)
    step += 1

# --------------------------

print("1. del: ")
print(total_flashes)
print("2. del: ")
print(step)




