import numpy as np


with open("day11.txt") as f:
    data = f.readline().strip().split(",")

# Delta coordinates
deltas = {"n": np.array([1, -1, 0]),
          "s": np.array([-1, 1, 0]),
          "nw": np.array([1, 0, -1]),
          "ne": np.array([0, -1, 1]),
          "sw": np.array([0, 1, -1]),
          "se": np.array([-1, 0, 1])}

# Starting position
pos = np.array([0, 0, 0])

# Furthest so far
furthest = 0

# Move
for move in data:
    pos += deltas[move]
    if max(np.abs(pos)) > furthest:
        furthest = max(np.abs(pos))
print("Furthest =", furthest)
