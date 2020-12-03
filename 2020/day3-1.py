import numpy as np

with open("day3.txt", "r") as f:
    map = f.read().splitlines()
move = np.array([1, 3])
pos = np.array([0, 0])

n_lines = len(map)
n_trees = 0
while pos[0] < n_lines - 1:
    pos += move
    pos[1] = np.mod(pos[1], len(map[0]))
    if map[pos[0]][pos[1]] == "#":
        n_trees += 1

print(n_trees)
