import numpy as np


with open("day1.txt") as f:
    data = f.readline().split(', ')

turn = {"L": np.matrix([[0, -1], [1, 0]]), "R": np.matrix([[0, 1], [-1, 0]])}

pos = np.matrix([[0], [0]])
dire = np.matrix([[-1], [0]])

for inst in data:
    dire = np.dot(turn[inst[0]], dire)
    pos += dire*int(inst[1:])

print("Result =", sum([abs(x) for x in np.array(pos)])[0])

