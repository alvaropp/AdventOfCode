import numpy as np


def process_opcode_and_param(number):
    param = str(number)
    opcode = int(param[-2:])
    mode = param[:-2]
    mode = "0" * (3 - len(mode)) + mode
    return opcode, mode[::-1]


def get_value(data, mode, pos):
    if mode == "0":
        return data[data[pos]]
    if mode == "1":
        return data[pos]


def go(data, pos, last_input):
    opcode, mode = process_opcode_and_param(data[pos])

    if opcode == 1:
        data[data[pos + 3]] = get_value(data, mode[0], pos + 1) + get_value(
            data, mode[1], pos + 2
        )
        pos += 4

    elif opcode == 2:
        data[data[pos + 3]] = get_value(data, mode[0], pos + 1) * get_value(
            data, mode[1], pos + 2
        )
        pos += 4

    elif opcode == 3:
        data[data[pos + 1]] = last_input
        pos += 2

    elif opcode == 4:
        last_input = get_value(data, mode[0], pos + 1)
        pos += 2

    elif opcode == 99:
        pos = -1

    else:
        raise ValueError

    return data, pos, last_input


data = np.genfromtxt("day5.txt", delimiter=",", dtype=int)

pos = 0
last_input = 1

while pos >= 0:
    data, pos, last_input = go(data, pos, last_input)

print(last_input)
