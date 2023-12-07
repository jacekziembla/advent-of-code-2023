from __future__ import annotations
from dataclasses import dataclass

with open("03/input.txt", "r") as file:
    lines = file.read().splitlines()

X_SIZE = len(lines)
Y_SIZE = len(lines[0])


@dataclass
class Point:
    x: int
    y: int
    range = None

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def get_range(self) -> list:
        if self.range is None:
            self.range = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    p = Point(self.x + i, self.y + j)
                    if 0 <= p.x < X_SIZE and 0 <= p.y < Y_SIZE:
                        self.range.append(p)
        return self.range

    def is_adjacent(self, other) -> bool:
        """ Generates list of adjacent points """
        return self in other.get_range()


# Generates set of positions of symbols
symbols = []
for line_index, line in enumerate(lines):
    for char_index, char in enumerate(line):
        if char != "." and not char.isdigit():
            symbols.append(Point(line_index, char_index))


def is_adjacent_to_any_symbol(p: Point) -> bool:
    """ Checks if point is adjacent to any of collected symbols """
    for s in symbols:
        if s.is_adjacent(p):
            return True
    return False


# Parse trough input, check if the number is adjacent to any of symbols
adjacent = []
for line_index, line in enumerate(lines):
    current_number = ""
    is_adjacent = False
    for char_index, char in enumerate(line):
        if char.isdigit():
            current_number += char
            current_point = Point(line_index, char_index)
            if is_adjacent_to_any_symbol(current_point):
                is_adjacent = True
        else:
            if is_adjacent:
                adjacent.append(int(current_number))
            current_number = ""
            is_adjacent = False
    if is_adjacent:
        adjacent.append(int(current_number))
        current_number = ""
        is_adjacent = False

# Part A
print(sum(adjacent))
