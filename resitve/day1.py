meritve = []
with open("input/day1.txt") as inp:
    for vrst in inp:
        meritve.append(int(vrst))

okna = []
for j in range(len(meritve)-2):
    okna.append(meritve[j] + meritve[j+1] + meritve[j+2])

def count_increase(sez):
    count = 0
    for i in range(1, len(sez)):
        if sez[i] > sez[i-1]:
            count += 1
    return count

# --------------------------

print("1. del: ")
print(count_increase(meritve))
print("2. del: ")
print(str(count_increase(okna)))