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

offsets = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

def level_of(pos):
    x, y = pos
    idx = rows[y][x]
    return levels[idx]

def valid(pos):
    x, y = pos
    return 0 <= x < width and 0 <= y < height

def can_move_to_neighbour(curr, neighbour):
    return level_of(neighbour) <= level_of(curr) + 1

def neighbours(pos):
    x, y = pos
    for dx, dy in offsets:
        neighbour = (x + dx), (y + dy)
        if valid(neighbour) and can_move_to_neighbour(pos, neighbour):
            yield neighbour

dist = {}
queue = SimpleQueue()
dist[S] = 0

queue.put(S)
while not queue.empty():
    pos = queue.get()
    x, y = pos

    for neighbour in neighbours(pos):
        if neighbour not in dist:
            dist[neighbour] = dist[pos] + 1
            queue.put(neighbour)

print(dist[E])




