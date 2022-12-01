with open("day01_input.txt") as f:
    elves = f.read().split("\n\n")
    elf_sums = (sum(int(x) for x in elf.split("\n") if x) for elf in elves)

first, second, third, *_ = sorted(elf_sums, reverse=True)
print(first)
print(first + second + third)