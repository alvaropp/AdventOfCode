import numpy as np

with open("day3.txt", "r") as f:
    map = f.read().splitlines()

moves = [
    np.array([1, 1]),
    np.array([1, 3]),
    np.array([1, 5]),
    np.array([1, 7]),
    np.array([2, 1]),
]

def count_trees(move):
    pos = np.array([0, 0])
    n_lines = len(map)
    n_trees = 0
    while pos[0] < n_lines - 1:
        pos[1] = np.mod(pos[1], len(map[0]))
        if map[pos[0]][pos[1]] == "#":
            n_trees += 1
        pos += move
    return n_trees

n_treess = []
for move in moves:
    n_treess.append(count_trees(move))

print(np.prod(n_treess))
