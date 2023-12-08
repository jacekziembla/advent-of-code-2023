from __future__ import annotations

with open("08/input.txt", "r") as file:
    lines = file.read().splitlines()

INSTRUCTION = lines[0]
LEN = len(INSTRUCTION)
NODES = {}
currents = []
DIRECTION = {
    "L": 0,
    "R": 1
}

for line in lines[2:]:
    node = line[0:3]
    left = line[7:10]
    right = line[12:15]
    NODES[node] = (left, right)
    if node.endswith("A"):
        currents.append(node)

step = 0
while not all([node.endswith("Z") for node in currents]):
    next_step_index = step % LEN
    next_step = INSTRUCTION[next_step_index]
    new_currents = []
    for current in currents:
        new_currents.append(NODES[current][DIRECTION[next_step]])
    currents = new_currents
    step += 1

print(step)
