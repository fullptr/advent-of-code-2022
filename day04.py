with open("day04_input.txt") as f:
    lines = f.readlines()

def contains(l1, l2, r1, r2):
    return (l1 <= r1 and l2 >= r2) or (r1 <= l1 and r2 >= l2)

def overlaps(l1, l2, r1, r2):
    return (l1 <= r1 <= l2) or (r1 <= l1 <= r2)

part1 = 0
part2 = 0
for line in lines:
    l, r = line.split(",")
    l1, l2 = (int(x) for x in l.split("-"))
    r1, r2 = (int(x) for x in r.split("-"))
    part1 += contains(l1, l2, r1, r2)
    part2 += overlaps(l1, l2, r1, r2)
print(part1)
print(part2)