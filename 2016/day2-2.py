import numpy as np


keypad = np.array([[0, 0, 1, 0, 0],
                   [0, 2, 3, 4, 0],
                   [5, 6, 7, 8, 9],
                   [0, 'A', 'B', 'C', 0],
                   [0, 0, 'D', 0, 0]])
pos = np.array([2, 0])
delta = {"U": np.array([-1, 0]),
         "R": np.array([0, 1]),
         "D": np.array([1, 0]),
         "L": np.array([0, -1])}
valid = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0], 
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 1, 1, 1, 1, 1, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]])

with open("day2.txt") as f:
    data = [x.strip() for x in f.readlines()]

code = []
for instruction in data:
    for letter in instruction:
        newPos = pos + delta[letter]
        if valid[newPos[0]+1, newPos[1]+1] == 1:
            pos = newPos.copy()
    code.append(keypad[pos[0], pos[1]])

print("Result =", "".join(str(x) for x in code))

