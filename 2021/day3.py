import numpy as np


def find_most_common_bit(bit_array):
    count = np.bincount(bit_array)
    if count[0] == count[1]:
        return 1
    else:
        return np.argmax(count)


def find_least_common_bit(bit_array):
    count = np.bincount(bit_array)
    if count[0] == count[1]:
        return 0
    else:
        return np.argmin(count)


with open("day3.txt", "r") as f:
    data = np.asarray(
        [[int(bit) for bit in list(line.strip())] for line in f.readlines()]
    )

gamma_rate = int(
    "".join(
        [
            str(bit)
            for bit in np.apply_along_axis(find_most_common_bit, axis=0, arr=data)
        ]
    ),
    2,
)
epsilon_rate = int(
    "".join(
        [
            str(bit)
            for bit in np.apply_along_axis(find_least_common_bit, axis=0, arr=data)
        ]
    ),
    2,
)
print(f"Part 1: {gamma_rate * epsilon_rate}")


with open("day3.txt", "r") as f:
    data = [[int(bit) for bit in list(line.strip())] for line in f.readlines()]


def eliminate(data, fnc):
    position = 0
    while len(data) > 1:
        most_common = fnc([row[position] for row in data])
        data = [row for row in data if row[position] == most_common]
        position += 1
    return int("".join([str(bit) for bit in data[0]]), 2)


oxygen = eliminate(data, find_most_common_bit)
co2 = eliminate(data, find_least_common_bit)

print(f"Part 2: {oxygen * co2}")
