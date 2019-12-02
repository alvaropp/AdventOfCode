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


data = np.genfromtxt("day2.txt", delimiter=",", dtype=int)
data[1] = 12
data[2] = 2

pos = 0
while pos >= 0:
    data, pos = go(data, pos)

print(data[0])
