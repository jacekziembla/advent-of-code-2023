from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional

with open("10/input.txt", "r") as file:
    lines = file.read().splitlines()


@dataclass
class Point:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def connections(self, symbol) -> List[Point]:
        north = Point(self.x - 1, self.y)
        south = Point(self.x + 1, self.y)
        west = Point(self.x, self.y - 1)
        east = Point(self.x, self.y + 1)
        match symbol:
            case "|":
                return [north, south]
            case "-":
                return [west, east]
            case "L":
                return [north, east]
            case "J":
                return [north, west]
            case "7":
                return [south, west]
            case "F":
                return [south, east]
            case ".":
                return []


MAP = {}
START = None
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        point = Point(x, y)
        MAP[point] = char
        if char == "S":
            START = point


def go_next(current_point: Point, previous_point: Point = None) -> Optional[Point]:
    connections = current_point.connections(symbol=MAP[current_point])
    if previous_point is not None:
        try:
            connections.remove(previous_point)
        except ValueError:  # Dead end
            return None
    return connections[0]


def find_cycle(potential_pipe: str) -> Optional[List[Point]]:
    MAP[START] = potential_pipe
    path = [START]
    current = START
    previous = None
    while True:
        next_node = go_next(current, previous)
        if next_node is None:  # Break if dead end
            return
        if START == next_node:  # Found cycle!
            break
        path.append(next_node)
        previous = current  # Shift by 1
        current = next_node  # Shift by 1
    return path


# Part One
potential_pipes = ["|", "-", "L", "J", "7", "F"]
for pipe in potential_pipes:
    if (found_path := find_cycle(potential_pipe=pipe)) is not None:
        print(int(len(found_path) / 2))
        break
