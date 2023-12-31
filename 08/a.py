from __future__ import annotations

with open("08/input.txt", "r") as file:
    lines = file.read().splitlines()

INSTRUCTION = lines[0]
LEN = len(INSTRUCTION)
NODES = {}
START = "AAA"
END = "ZZZ"
DIRECTION = {
    "L": 0,
    "R": 1
}

for line in lines[2:]:
    node = line[0:3]
    left = line[7:10]
    right = line[12:15]
    NODES[node] = (left, right)

current = START
step = 0
while current != END:
    next_step_index = step % LEN
    next_step = INSTRUCTION[next_step_index]
    current = NODES[current][DIRECTION[next_step]]
    step += 1

print(step)
