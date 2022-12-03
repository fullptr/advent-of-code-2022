with open("day02_input.txt") as f:
    lines = f.readlines()

wins = {"A": "B", "B": "C", "C": "A"} # value beats key
loses = {v: k for k, v in wins.items()} # key beats value
scores = {"A": 1, "B": 2, "C": 3}
p1map = {"X": "A", "Y": "B", "Z": "C"}

def game(l, r): # l and r are both in {A, B, C}
    if (l, r) in wins.items():
        return scores[r] + 6
    elif l == r:
        return scores[r] + 3
    return scores[r]

total1 = 0
total2 = 0
for line in lines:
    l, r = line.split()
    total1 += game(l, p1map[r])
    if r == "X":
        total2 += game(l, loses[l])
    elif r == "Y":
        total2 += game(l, l)
    else:
        total2 += game(l, wins[l])

print(total1)
print(total2)