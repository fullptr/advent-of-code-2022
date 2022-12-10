from queue import Queue
from more_itertools import grouper
with open("day10_input.txt") as f:
    data = (l.strip() for l in f.readlines())

jobs = Queue()

for line in data:
    match line.split():
        case ["noop"]: jobs.put([1, 0]) # steps, addx value
        case ["addx", value]: jobs.put([2, int(value)])

reg = 1
cycle = 1
signal_sum = 0
crt_screen = [" " for _ in range(40*6)]

current_job = jobs.get()
while current_job:
    if cycle % 40 - 20 == 0: # part 1
        signal_sum += cycle * reg
    if abs((cycle - 1) % 40 - reg) <= 1: # part 2
        crt_screen[cycle - 1] = '█'

    current_job[0] -= 1 # tick down
    if current_job[0] == 0:
        reg += current_job[1]
        current_job = jobs.get() if not jobs.empty() else None
    cycle += 1

print(signal_sum)
for row in grouper(crt_screen, 40):
    print("".join(row))