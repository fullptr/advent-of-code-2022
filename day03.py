with open("day03_input.txt") as f:
    lines = [l.strip() for l in f]

def triples(iterable):
    args = [iter(iterable)] * 3
    return zip(*args, strict=True)

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities = {letter: idx + 1 for idx, letter in enumerate(letters)}

part1 = 0
for line in lines:
    first_half = set(line[:len(line)//2])
    second_half = set(line[len(line)//2:])
    part1 += priorities[(first_half & second_half).pop()]
print(part1)

part2 = 0
for a, b, c in triples(lines):
    part2 += priorities[(set(a) & set(b) & set(c)).pop()]
print(part2)