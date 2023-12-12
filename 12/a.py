from __future__ import annotations

from dataclasses import dataclass
from typing import List
from itertools import product

with open("12/input.txt", "r") as file:
    lines = file.read().splitlines()

OPERATIONAL = "."
DAMAGED = "#"
UNKNOWN = "?"


def generate_unknowns(size: int):
    if size == 0:
        return []
    return ["".join(i) for i in product([OPERATIONAL, DAMAGED], repeat=size)]


@dataclass
class Row:
    text: str
    sizes: List[int]

    def get_unknown_indexes(self) -> List[int]:
        return [i for i, char in enumerate(self.text) if char == UNKNOWN]

    def validate(self) -> bool:
        springs = self.text.replace(".", " ").split()
        return [len(spring) for spring in springs] == self.sizes


valid = []
for index, line in enumerate(lines):
    actually_valid = 0
    left, right = line.split()
    sizes = [int(s) for s in right.split(",")]
    row = Row(text=left, sizes=sizes)
    unknowns = row.get_unknown_indexes()
    possibilities = generate_unknowns(size=len(unknowns))
    if unknowns == 0:
        valid.append(1)
        continue
    for possibility in possibilities:
        new_text = list(row.text)
        for i, unknown_index in enumerate(unknowns):
            new_text[unknown_index] = possibility[i]
        new_text = "".join(new_text)
        new_row = Row(new_text, sizes)
        if new_row.validate():
            actually_valid += 1
    valid.append(actually_valid)
    print(f"{index}: {actually_valid}")

print(sum(valid))
