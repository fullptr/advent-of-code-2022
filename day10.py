from queue import Queue
from more_itertools import grouper
with open("day10_input.txt") as f:
    data = (l.strip() for l in f.readlines())

jobs = Queue()

for line in data:
    match line.split():
        case ["noop"]: jobs.put(["noop", 1])
        case ["addx", value]: jobs.put(["addx", 2, int(value)])

reg = 1
current_job = None
cycle = 1
signal_sum = 0

crt_screen = [" " for _ in range(40*6)]

while not jobs.empty() or current_job is not None:
    if current_job is None and not jobs.empty():
        current_job = jobs.get()

    if cycle % 40 - 20 == 0:
        signal_sum += cycle*reg
    if abs((cycle - 1) % 40 - reg) <= 1:
        crt_screen[cycle - 1] = '█'

    current_job[1] -= 1 # tick down
    if current_job[1] == 0:
        match current_job[0]:
            case "noop": pass
            case "addx": reg += current_job[2]
        current_job = None

    cycle += 1

print(signal_sum)
for row in grouper(crt_screen, 40):
    print("".join(row))