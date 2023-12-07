from typing import List, Dict

with open("02/input.txt", "r") as file:
    lines = file.read().splitlines()


def game_parser(game_line: str) -> List[Dict[str, int]]:
    sets = game_line.split(":")[1].split(";")
    list_of_sets = []
    for s in sets:
        set_map = {}
        cubes = s.split(",")
        for cube in cubes:
            cube = cube.lstrip().split()
            number = int(cube[0])
            color = cube[1]
            set_map[color] = number
        list_of_sets.append(set_map)
    return list_of_sets


def validate_game_feasibility(game: List[Dict[str, int]]) -> bool:
    validity_map = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for game_set in game:
        for color, value in game_set.items():
            if value > validity_map[color]:
                return False
    return True


games = []
for line in lines:
    games.append(game_parser(line))

# Part A
valid_games = []
for index, current_game in enumerate(games):
    if validate_game_feasibility(current_game):
        valid_games.append(index + 1)
print(sum(valid_games))


# Part B
def calculate_max_cubes(game: List[Dict[str, int]]) -> Dict[str, int]:
    cubes = {}
    for game_set in game:
        for color, value in game_set.items():
            if value > cubes.get(color, 0):
                cubes[color] = value
    return cubes


def calculate_power(cubes: Dict[str, int]) -> int:
    ret = 1
    for value in cubes.values():
        ret = ret * value
    return ret


powers = []
for index, current_game in enumerate(games):
    min_cubes = calculate_max_cubes(current_game)
    powers.append(calculate_power(min_cubes))
print(sum(powers))
