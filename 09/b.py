from __future__ import annotations

from typing import List

with open("09/input.txt", "r") as file:
    lines = file.read().splitlines()


def get_diffs(original_row: List[int]) -> List[int]:
    """ Gets row one level deeper """
    diff_row = []
    for i in range(1, len(original_row)):
        diff_row.append(original_row[i] - original_row[i - 1])
    return diff_row


def is_row_zero(original_row: List[int]) -> bool:
    return all(element == 0 for element in original_row)


counter = 0
for line in lines:
    row = [int(n) for n in line.split()]
    rows = []
    while not is_row_zero(row):
        rows.append(row)
        row = get_diffs(row)
    extra_element = 0
    for i in range(len(rows)):
        current_row = rows[-1 - i]
        extra_element = current_row[0] - extra_element
        current_row.insert(0, extra_element)
    counter += extra_element

print(counter)
