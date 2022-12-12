import parse
import math
from dataclasses import dataclass, field
with open("day11_input.txt") as f:
    data = f.read()

monkey_match = """Monkey {num}:
  Starting items: {items}
  Operation: new = old {formula}
  Test: divisible by {test:d}
    If true: throw to monkey {if_true:d}
    If false: throw to monkey {if_false:d}"""

@dataclass
class Monkey:
    items: field(default_factory=list)
    formula: str
    test: int
    if_true: int
    if_false: int
    num_inspects: int = 0

def apply_formula(formula: str, old: int) -> int:
    if formula.startswith("+"):
        return old + int(formula.removeprefix("+ "))
    if formula == "* old":
        return old * old
    return old * int(formula.removeprefix("* "))

def get_monkeys() -> list[Monkey]:
    monkeys: list[Monkey] = []
    for monkey_data in data.split("\n\n"):
        matcher = parse.search(monkey_match, monkey_data)
        monkeys.append(Monkey(
            items = [int(x) for x in matcher["items"].split(", ")],
            formula = matcher["formula"],
            test = matcher["test"],
            if_true = matcher["if_true"],
            if_false = matcher["if_false"]
        ))
    return monkeys


def run_sim(monkeys: list[Monkey], iterations: int, relief_func):
    for _ in range(iterations):
        for m in monkeys:
            for item in m.items:
                item = apply_formula(m.formula, item)
                item = relief_func(item)
                m.num_inspects += 1
                throw_to = m.if_true if item % m.test == 0 else m.if_false
                monkeys[throw_to].items.append(item)
            m.items = []
    *_, a, b = sorted(monkeys, key=lambda m: m.num_inspects)
    print(a.num_inspects * b.num_inspects)

monkeys = get_monkeys()
run_sim(monkeys, 20, lambda x: x // 3)

monkeys = get_monkeys()
factor = math.prod(m.test for m in monkeys)
run_sim(monkeys, 10000, lambda x: x % factor)