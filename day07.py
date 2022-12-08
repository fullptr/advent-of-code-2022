from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

@dataclass
class File:
    name: str
    size: int

Filesystem = dict[Path, list[Path | File]]

with open("day07_input.txt") as f:
    lines = f.readlines()

def get_dirsize(dirname: Path, fs: Filesystem):
    dirsize = 0
    for file in fs[dirname]:
        match file:
            case File(_, size):
                dirsize += size
            case Path as p:
                dirsize += get_dirsize(p, fs)
    return dirsize

current_path = Path("/")
fs: dict[Path, list[Path | File]] = defaultdict(list)

for line in lines:
    match line.split():
        case ["$", "cd", "/"]:
            current_path = Path("/")
        case ["$", "cd", ".."]:
            current_path = current_path.parent
        case ["$", "cd", dirname]:
            current_path = current_path / dirname
        case ["$", "ls"]:
            pass
        case ["dir", subdir]:
            fs[current_path].append(current_path / subdir)
        case [size, file] if size.isdigit():
            fs[current_path].append(File(name=file, size=int(size)))

unused_space = 70000000 - get_dirsize(Path("/"), fs)
space_to_free = 30000000 - unused_space

part1 = 0
part2 = float("inf")
for directory, files in fs.items():
    size = get_dirsize(directory, fs)
    if size <= 100000:
        part1 += size
    if space_to_free <= size < part2:
        part2 = size

print(part1)
print(part2)