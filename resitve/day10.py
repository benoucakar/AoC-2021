lines = []
with open("input/day10.txt") as inp:
    for vrst in inp:
        lines.append(list(vrst[:-1]))

C_scores = {"C)": 3, "C]": 57, "C}": 1197, "C>": 25137}
end_scores = {")": 1, "]": 2, "}": 3, ">": 4}

def fix(line):
    spomin = []
    for z in line:
        if z in ["(","[","{","<"]:
            spomin.append(z)
        if z == ")":
            if spomin[-1] == "(":
                spomin.pop(-1)
            else:
                return "C)"
        if z == "]":
            if spomin[-1] == "[":
                spomin.pop(-1)
            else:
                return "C]"
        if z == "}":
            if spomin[-1] == "{":
                spomin.pop(-1)
            else:
                return "C}"
        if z == ">":
            if spomin[-1] == "<":
                spomin.pop(-1)
            else:
                return "C>"
    end = ""
    while len(spomin) > 0:
        zadnji_znak = spomin.pop(-1)
        if zadnji_znak == "(": end += ")"
        if zadnji_znak == "[": end += "]"
        if zadnji_znak == "{": end += "}"
        if zadnji_znak == "<": end += ">"
    return end

def end_score(end):
    score = 0
    for z in list(end):
        score *= 5
        score += end_scores[z]
    return score

C_score = 0
ends = []     
for outpt in [fix(line) for line in lines]:
    if outpt in ["C)","C]","C}","C>"]:
        C_score += C_scores[outpt]
    else:
        ends.append(outpt)

# --------------------------

print("1. del: ")
print(C_score)
print("2. del: ")
print(sorted([end_score(end) for end in ends])[len(ends)//2])