from more_itertools import sliding_window
with open("day06_input.txt") as f:
    data = f.read().strip()

def find_marker(data, size):
    for idx, chars in enumerate(sliding_window(data, size), size):
        if len(set(chars)) == size:
            return idx

print(find_marker(data, 4))
print(find_marker(data, 14))