import numpy as np


with open("day1.txt") as f:
    data = f.readline().split(', ')

turn = {"L": np.matrix([[0, -1], [1, 0]]), "R": np.matrix([[0, 1], [-1, 0]])}

pos = np.matrix([[0], [0]])
oldPoss = [pos.copy()]
dire = np.matrix([[-1], [0]])

j = 0
while j < len(data):
    inst = data[j]
    dire = np.dot(turn[inst[0]], dire)
    for i in range(int(inst[1:])):
        pos += dire
        try:
            ind = next((i for i, val in enumerate(oldPoss) if np.all(val==pos)))
            j = len(data)
            break
        except:
            pass
        oldPoss.append(pos.copy())
    j += 1

print("Solution =", sum([abs(x) for x in np.array(pos)])[0])

