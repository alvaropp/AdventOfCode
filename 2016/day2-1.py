import numpy as np


keypad = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
pos = np.array([1, 1])
delta = {"U": np.array([-1, 0]),
         "R": np.array([0, 1]),
         "D": np.array([1, 0]),
         "L": np.array([0, -1])}

with open("day2.txt") as f:
    data = [x.strip() for x in f.readlines()]

code = []
for instruction in data:
    for letter in instruction:
        newPos = pos + delta[letter]
        if np.sum((newPos >= 0) & (newPos <= 2)) == 2:
            pos = newPos.copy()
    code.append(int(keypad[pos[0], pos[1]]))

print("Result =", "".join(str(x) for x in code))

