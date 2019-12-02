import numpy as np


def go(data, pos):
    if data[pos] == 1:
        data[data[pos + 3]] = data[data[pos + 1]] + data[data[pos + 2]]
        pos += 4
    elif data[pos] == 2:
        data[data[pos + 3]] = data[data[pos + 1]] * data[data[pos + 2]]
        pos += 4
    elif data[pos] == 99:
        pos = -1
    else:
        raise ValueError
    return data, pos


for noun in range(100):
    for verb in range(100):
        data = np.genfromtxt("day2.txt", delimiter=",", dtype=int)
        data[1] = noun
        data[2] = verb
        pos = 0
        while pos >= 0:
            data, pos = go(data, pos)
        if data[0] == 19690720:
            print(100 * noun + verb)
            break
