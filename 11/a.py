from __future__ import annotations
from dataclasses import dataclass

with open("11/input.txt", "r") as file:
    lines = file.read().splitlines()

DIFF = 1 # PART A
DIFF = 999999 # PART B

rows_to_expand = []
columns_to_expand = []
for index, row in enumerate(lines):
    if "#" not in row:
        rows_to_expand.append(index)

transposed_lines = [list(row) for row in zip(*lines)]
for index, column in enumerate(transposed_lines):
    if "#" not in column:
        columns_to_expand.append(index)


@dataclass
class Point:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __sub__(self, other) -> int:
        normal_dist = abs(self.x - other.x) + abs(self.y - other.y)
        extra_dist = 0
        for row in rows_to_expand:
            if self.x < row < other.x:
                extra_dist += DIFF
        for col in columns_to_expand:
            if self.y < col < other.y:
                extra_dist += DIFF
        return normal_dist + extra_dist * 2


points = {}
i = 1
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char == "#":
            points[i] = Point(x, y)
            i += 1

distances = []
for p1 in range(1, i):
    for p2 in range(1, i):
        diff = points[p1] - points[p2]
        # print(f"{p1}-{p2}: {diff}")
        distances.append(diff)

print(int(sum(distances) / 2))


