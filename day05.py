import parse
import copy
with open("day05_input.txt") as f:
    lines = (l.replace("\n", "") for l in f.readlines())

def move1(columns, count, src, dst):
    for _ in range(count):
        columns[dst].append(columns[src].pop())

def move2(columns, count, src, dst):
    columns[src], temp = columns[src][0:-count], columns[src][-count]
    #temp = [columns[src].pop() for _ in range(count)]
    columns[dst].extend(reversed(temp))

columns1 = []
commands = []
for line in lines:
    if line.strip().startswith("["):
        line = line[1::4]
        if len(columns1) == 0: # init column list
            columns1 = [[] for _ in line]
        for idx, char in enumerate(line):
            if char != " ":
                columns1[idx].append(char)
        pass
    elif line.startswith("move"):
        match = parse.parse("move {move:d} from {from:d} to {to:d}", line)
        commands.append((match["move"], match["from"]-1, match["to"]-1))

for column in columns1:
    column.reverse()

columns2 = copy.deepcopy(columns1)

for count, src, dst in commands:
    move1(columns1, count, src, dst)
    move2(columns2, count, src, dst)

print("".join(c[-1] for c in columns1))
print("".join(c[-1] for c in columns2))