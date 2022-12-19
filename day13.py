import json
with open("day13_input.txt") as f:
    data = f.read()

def compare(lhs, rhs, indent = 0):
    #print(f"{' '*indent}- Compare {lhs} vs {rhs}")
    match lhs, rhs:
        case [int(l), int(r)]:
            if l < r:
                #print(f"{' '*(indent + 1)}- Left side is smaller, so inputs are in the right order")
                return True
            if l > r:
                #print(f"{' '*(indent + 1)}- Right side is smaller, so inputs are not in the right order")
                return False
            return None
        case [list(l), int(r)]:
            #print(f"{' '*(indent + 1)}- Mixed types; convert right to {[r]} and retry comparison")
            return compare(l, [r], indent+1)
        case [int(l), list(r)]:
            #print(f"{' '*(indent + 1)}- Mixed types; convert left to {[l]} and retry comparison")
            return compare([l], r, indent+1)
        case [list(l), list(r)]:
            for a, b in zip(l, r):
                val = compare(a, b, indent+1)
                if val is not None:
                    return val
            if len(r) < len(l):
                #print(f"{' '*(indent + 1)}- Right side ran out of items, so inputs are not in the right order")
                return False
            if len(r) > len(l):
                #print(f"{' '*(indent + 1)}- Left side ran out of items, so inputs are in the right order")
                return True
            return None

packets = []

part1 = 0
for idx, pair in enumerate(data.split("\n\n"), 1):
    a, b = pair.split("\n")
    #print(f"== Pair {idx} ==")
    A = json.loads(a)
    B = json.loads(b)
    if compare(A, B):
        part1 += idx
    packets.append(A)
    packets.append(B)
    #print()

print(f"Part 1: {part1}")

div1 = [[2]]
div2 = [[6]]
div1_less = 1 # start at index 1
div2_less = 2 # start at index 1, +1 extra to compare against [[2]]
for packet in packets:
    if compare(packet, div1):
        div1_less += 1
    if compare(packet, div2):
        div2_less += 1

print(f"Part 2: {div1_less * div2_less}")

    



