import math

with open("04/input.txt", "r") as file:
    lines = file.read().splitlines()

scores = winning = []
for index, line in enumerate(lines):
    left_str, right_str = line.split(":")[1].split("|")
    winning = {int(number) for number in left_str.split()}
    actual = {int(number) for number in right_str.split()}
    matching = len(actual.intersection(winning))
    score = 2 ** (matching - 1) if matching else 0
    scores.append(score)

# Part A
print(sum(scores))


# Part B
def get_matching_from_score(number: int) -> int:
    if number == 0:
        return 0
    return int(math.log(number, 2)) + 1


# List that stores occurrence of each card with some padding at the end
multipliers = [1 for _ in range(len(lines) + len(winning))]
for index, score in enumerate(scores):
    next_card_index = index + 1
    current_card_multiplayer = multipliers[index]
    if score != 0:
        extra_cards_range = list(range(next_card_index, next_card_index + get_matching_from_score(score)))
        for i in extra_cards_range:
            multipliers[i] += current_card_multiplayer

# Removing padding from the end
multipliers = multipliers[:len(scores)]

print(sum(multipliers))
