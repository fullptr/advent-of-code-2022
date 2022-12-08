import math
with open("day08_input.txt") as f:
    grid = [l.strip() for l in f.readlines()]

width = len(grid[0])
height = len(grid)

def walk(x, y, dx, dy):
    x += dx
    y += dy
    while 0 <= x < width and 0 <= y < height:
        yield grid[y][x]
        x += dx
        y += dy

def seen_from(x, y, dx, dy):
    for tree in walk(x, y, dx, dy):
        if tree >= grid[y][x]:
            return False
    return True

def count_from(x, y, dx, dy):
    count = 0
    for tree in walk(x, y, dx, dy):
        count += 1
        if tree >= grid[y][x]:
            break
    return count

def neighbours(x, y, func):
    return [
        func(x, y, 0, -1),
        func(x, y, -1, 0),
        func(x, y, 1, 0),
        func(x, y, 0, 1)
    ]

def seen(x, y):
    return any(neighbours(x, y, seen_from))

def scenic_score(x, y):
    return math.prod(neighbours(x, y, count_from))

part1 = 0
part2 = 0
for y in range(height):
    for x in range(width):
        part1 += seen(x, y)
        part2 = max(part2, scenic_score(x, y))
print(part1)
print(part2)