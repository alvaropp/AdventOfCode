from itertools import permutations
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
    delete = False
    output = None

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
        delete = True
        pos += 2

    elif opcode == 4:
        output = get_value(data, mode[0], pos + 1)
        pos += 2

    elif opcode == 5:
        if get_value(data, mode[0], pos + 1) != 0:
            pos = get_value(data, mode[1], pos + 2)
        else:
            pos += 3

    elif opcode == 6:
        if get_value(data, mode[0], pos + 1) == 0:
            pos = get_value(data, mode[1], pos + 2)
        else:
            pos += 3

    elif opcode == 7:
        value = (
            1
            if get_value(data, mode[0], pos + 1) < get_value(data, mode[1], pos + 2)
            else 0
        )
        data[data[pos + 3]] = value
        pos += 4

    elif opcode == 8:
        value = (
            1
            if get_value(data, mode[0], pos + 1) == get_value(data, mode[1], pos + 2)
            else 0
        )
        data[data[pos + 3]] = value
        pos += 4

    elif opcode == 99:
        pos = -1

    else:
        raise ValueError

    return data, pos, delete, output


def solve_amplifier(data, phase, last_input):

    inputs = [last_input, phase]

    last_output = None
    pos = 0
    while pos >= 0:
        data, pos, delete, output = go(data, pos, inputs[-1])
        if output:
            last_output = output
        if delete and len(inputs) == 2:
            inputs.pop()

    return last_output


def solve(data_base, phases):
    data = data_base.copy()
    _input = 0
    for phase in phases:
        _input = solve_amplifier(data, phase, _input)
    return _input


data_base = np.genfromtxt("day7.txt", delimiter=",", dtype=int)

max_result = -float("Inf")
for phases in list(permutations(range(5))):
    result = solve(data_base, phases)
    if result > max_result:
        max_result = result

print(max_result)
