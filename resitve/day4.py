class Bingo:
    def __init__(self, polje):
        self.done = False
        self.karta = polje
        self.spomin = [[False for _ in range(5)] for _ in range(5)]
    def pobarvaj(self, stv):
        for i in range(5):
            for j in range(5):
                if self.karta[i][j] == stv:
                    self.spomin[i][j] = True
    def preveri(self):
        for i in range(5):
            if all(self.spomin[i]):
                return True
        for j in range(5):
            if all([L[j] for L in self.spomin]):
                return True
        return False
    def score(self, stv):
        acc = 0
        for i in range(5):
            for j in range(5):
                if not self.spomin[i][j]:
                    acc += self.karta[i][j]
        return acc*stv

stevila = []
polja = []
with open("input/day4.txt") as inp:
    frst = True
    for vrst in inp:
        if frst:
            stevila = [int(x) for x in vrst[:-1].split(",")]
            frst = False
        else:
            if vrst == "\n":
                temp = []
            else:
                necista_vrst = vrst[:-1].split(" ")
                while "" in necista_vrst:
                    necista_vrst.remove("")
                temp.append([int(x) for x in necista_vrst])
            if len(temp) == 5:
                karta = Bingo(temp)
                polja.append(karta)

win_scores = []
for num in stevila:
    for polje in polja:
        if polje.done == True:
            continue
        polje.pobarvaj(num)
        if polje.preveri():
            polje.done = True
            win_scores.append(polje.score(num))

# --------------------------

print("1. del: ")
print(win_scores[0])
print("2. del: ")
print(win_scores[-1])
    
    
