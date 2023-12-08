from dataclasses import dataclass, field
from typing import Tuple
from copy import deepcopy

with open("05/input.txt", "r") as file:
    lines = file.read().splitlines()


@dataclass
class Range:
    destination: int
    source: int
    length: int

    def convert(self, number) -> int:
        diff = number - self.source
        if 0 <= diff < self.length:
            return self.destination + diff
        return number


@dataclass
class Map:
    name: Tuple[str, str]
    ranges: list = field(default_factory=lambda: [])

    def convert(self, number) -> int:
        """ Converts number """
        for r in self.ranges:
            value = r.convert(number)
            if value != number:
                return value
        return number


# Parse input
seeds_line = lines[0].split(": ")[1]
seeds = [int(n) for n in seeds_line.split()]
maps = []
current_map = None
for line in lines[2:]:
    if not bool(line):
        maps.append(current_map)
        current_map = None
        continue
    if not current_map:
        a, b = line.split(" ")[0].split("-to-")
        current_map = Map(name=(a, b))
        continue
    current_range = Range(*[int(n) for n in line.split()])
    current_map.ranges.append(current_range)
maps.append(current_map)

# iterate over maps and transform seed over each map
for map in maps:
    new_seed_values = []
    for seed in seeds:
        new_value = map.convert(number=seed)
        new_seed_values.append(new_value)
    seeds = deepcopy(new_seed_values)

# Part A answer
print(min(seeds))