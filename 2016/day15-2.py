import numpy as np


with open("day15.txt", "r") as f:
    discs = f.read().splitlines()
n_pos = np.array([int(disc.split("has ")[1].split(" pos")[0]) for disc in discs])
pos = np.array([int(disc[-2]) for disc in discs])
n_pos = np.append(n_pos, 11)
pos = np.append(pos, 0)
offset = np.arange(1, len(discs) + 2)

t = 0
while sum((pos + offset) % n_pos) > 0:
    pos = (pos + 1) % n_pos
    t += 1

print(t)
