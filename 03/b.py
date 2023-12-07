from __future__ import annotations
from dataclasses import dataclass
from collections import defaultdict

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


def __hash__(self) -> int:
    return hash((self.x, self.y))


def get_range(self) -> list:
    """ Generates list of adjacent points """
    if self.range is None:
        self.range = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                p = Point(self.x + i, self.y + j)
                if 0 <= p.x < X_SIZE and 0 <= p.y < Y_SIZE:
                    self.range.append(p)
    return self.range


def is_adjacent(self, other) -> bool:
    return self in other.get_range()


# Generates set of positions of symbols, also possible symbols
symbols = []
for line_index, line in enumerate(lines):
    for char_index, char in enumerate(line):
        if char == "*":
            symbols.append(Point(line_index, char_index))


def get_adjacent_symbols(p: Point, adjacent: set) -> None:
    """ Checks to which symbols specific point is adjacent to """
    for s in symbols:
        if s.is_adjacent(p):
            adjacent.add(s)


# Parse trough input, get list of numbers and adjacent symbols to these numbers
numbers = []
for line_index, line in enumerate(lines):
    current_number = ""
    adjacent_symbols = set()
    for char_index, char in enumerate(line):
        if char.isdigit():
            current_number += char
            current_point = Point(line_index, char_index)
            get_adjacent_symbols(current_point, adjacent_symbols)
        else:
            if adjacent_symbols:
                numbers.append((current_number, adjacent_symbols))
            adjacent_symbols = set()
            current_number = ""
    if adjacent_symbols:
        numbers.append((current_number, adjacent_symbols))
    adjacent_symbols = set()
    current_number = ""

# Get map symbol_position -> list of numbers
symbol_map = defaultdict(list)
for number, symbols in numbers:
    for symbol in symbols:
        symbol_map[symbol].append(int(number))

# Iterate over (symbol) -> (adjacent_numbers) pairs and get only the ones with two numbers
ratios = []
for symbol, numbers in symbol_map.items():
    if len(numbers) == 2:
        ratios.append(numbers[0] * numbers[1])
print(sum(ratios))
