with open("06/input.txt", "r") as file:
    lines = file.read().splitlines()

times = [int(n) for n in lines[0].split(":")[1].strip().split()]
distances = [int(n) for n in lines[1].split(":")[1].strip().split()]


def calc_distance(time, v):
    racing_time = time - v
    distance = racing_time * v
    return distance


def can_make_it(distance, time, v):
    possible_distance = calc_distance(time, v)
    return possible_distance > distance


def possible_velo(distance, time):
    possible_values = []
    for velo in range(1, distance + 1):
        if found := can_make_it(distance, time, velo):
            possible_values.append(velo)
        if possible_values and not found:
            break
    return possible_values


value = 1
for i in range(len(times)):
    value *= len(possible_velo(distance=distances[i], time=times[i]))

print(value)

# Part B
t = int("".join([str(n) for n in times]))
d = int("".join([str(n) for n in distances]))
print(len(possible_velo(d, t)))
