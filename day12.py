from queue import SimpleQueue
with open("day12_input.txt") as f:
    rows = [l.strip() for l in f]
    height = len(rows)
    width = len(rows[0])

abc = "abcdefghijklmnopqrstuvwxyz"
levels = {letter: idx for idx, letter in enumerate(abc)}
levels["S"] = 0
levels["E"] = 25

def find(c):
    for y in range(height):
        for x in range(width):
            if rows[y][x] == c:
                return (x, y)

S = find("S")
E = find("E")

def level_of(pos):
    x, y = pos
    idx = rows[y][x]
    return levels[idx]

def valid(pos):
    x, y = pos
    return 0 <= x < width and 0 <= y < height

# Neighbour can either climb up 1 to us, or drop down to us
def can_move_from_neighbour(curr, neighbour):
    return level_of(curr) - 1 <= level_of(neighbour)

def neighbours(x, y):
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        neighbour = (x + dx), (y + dy)
        if valid(neighbour) and can_move_from_neighbour((x, y), neighbour):
            yield neighbour

dist = {}
queue = SimpleQueue()
dist[E] = 0

queue.put(E)
while not queue.empty():
    x, y = queue.get()
    for neighbour in neighbours(x, y):
        if neighbour not in dist:
            dist[neighbour] = dist[x, y] + 1
            queue.put(neighbour)

print(dist[S])
min_dist = dist[S]
for (x, y), distance in dist.items():
    if rows[y][x] == "a" and distance < min_dist:
        min_dist = distance

print(min_dist)




